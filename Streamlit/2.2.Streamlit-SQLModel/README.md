# Streamlit-SQLModel

## AI Chat Bot

This project allows you to chat with AI.<br>
Link: https://sina-chatbot.streamlit.app/
## Local Run

At first, you must install all the required libraries that are in the `requirements.txt` file with the following command:

```
pip install -r requirements.txt
```

### Run

Then you need to create a local database with Docker and connect it to your application:

- Set `PostgreSQL` database url variable:

```
DATABASE_URL = "postgresql://sina:ramze_sina@localhost:5432/database_sina"
```

- Docker pull postgres

```
docker pull postgres
```

Run `PostgreSQL` docker container:

```
docker run -p 5432:5432 --name some-postgres -e POSTGRES_PASSWORD=ramze_sina -e POSTGRES_USER=sina -e POSTGRES_DB=database_sina -d postgres
```
