import requests
import json
import streamlit as st
from os import getenv
from dotenv import load_dotenv
from sqlmodel import Field, Session, SQLModel, create_engine, select, Relationship
from models import User, Message
from database import create_db_tables, engine, create_user, authenticate_user, select

dotenv = load_dotenv()
API_key = getenv("API_key")

create_db_tables()


@st.cache_resource
def connect_to_database():
    return engine


engine = connect_to_database()


def ai(prompt: str) -> str:
    headers = {"Authorization": f"Bearer {API_key}"}
    url = "https://api.edenai.run/v2/text/chat"
    payload = {
        "providers": "openai",
        "text": prompt,
        "chatbot_global_action": "Act as an assistant",
        "previous_history": [],
        "temperature": 0.0,
        "max_tokens": 150,
        "fallback_providers": "OpenAI - gpt-3.5-turbo, OpenAI - gpt-3.5-turbo-1106, OpenAI , OpenAI - gpt-3.5-turbo-0301"
    }

    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)

    print(result)

    if response.status_code == 200:
        if 'openai' in result and 'generated_text' in result['openai']:
            generated_text = result['openai']['generated_text']
            return generated_text
        else:
            error_message = "Error: 'openai' or 'generated_text' key not found in response"
            print(error_message)
            return "Error: Unable to fetch response from Eden AI"
    else:
        error_message = f"Error: {response.status_code} - {response.text}"
        print(error_message)
        return "Error: Unable to fetch response from Eden AI"


def process(user_text_message, user_id):
    try:
        ai_text_message = ai(user_text_message)

        user_message = Message(text=user_text_message,
                               type='user', user_id=user_id)
        ai_message = Message(text=ai_text_message, type='ai', user_id=user_id)

        # back-end
        with Session(engine) as session:
            session.add(user_message)
            session.add(ai_message)
            session.commit()
    except Exception as e:
        st.error(f"Error in process function: {e}")
        print(f"Error in process function: {e}")


def get_user_messages(user_id):
    try:
        with Session(engine) as session:
            statement = select(Message).where(Message.user_id == user_id)
            messages = session.exec(statement).all()
        return messages
    except Exception as e:
        st.error(f"Error in get_user_messages function: {e}")
        print(f"Error in get_user_messages function: {e}")
        return []


if 'user' not in st.session_state:
    st.session_state.user = None

with st.sidebar:
    if st.session_state.user is None:
        choice = st.selectbox('Choose Action', ['Login', 'Sign Up'])

        if choice == "Sign Up":
            st.subheader("Create a new account")
            name = st.text_input("Name")
            email = st.text_input("Email")
            password = st.text_input("Password", type='password')

            if st.button("Sign Up"):
                user = create_user(name, email, password)
                if user:
                    st.success("Account created successfully!")
                    st.session_state.user = user
                else:
                    st.error("User with this email already exists.")

        elif choice == "Login":
            st.subheader("Login to your account")
            email = st.text_input("Email")
            password = st.text_input("Password", type='password')

            if st.button("Login"):
                user = authenticate_user(email, password)
                if user:
                    st.success("Login successful!")
                    st.session_state.user = user
                else:
                    st.error("Invalid email or password")

    if st.session_state.user:
        st.write(f'Welcome, {st.session_state.user.name}')
        if st.button("Logout"):
            st.session_state.user = None
            st.experimental_rerun()

if st.session_state.user:
    messages = get_user_messages(st.session_state.user.id)
    for message in messages:
        with st.chat_message(message.type):
            st.write(message.text)

if user_text_message := st.chat_input("Send a new message..."):
    process(user_text_message, st.session_state.user.id)

    with st.chat_message('user'):
        st.write(user_text_message)

    with st.chat_message('ai'):
        st.write(ai(user_text_message))
