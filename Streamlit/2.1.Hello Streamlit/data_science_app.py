import streamlit as st
import pandas as ps

st.title("Simple Data Science App")

uploaded_file = st.file_uploader("Choose a .csv ... ", type=('.csv'))
if uploaded_file is not None:
    st.success("فایل با موفقیت بارگذاری شد.")
    data_frame = ps.read_csv(uploaded_file)

    st.write('### Data Frame')
    st.write(data_frame)

    st.sidebar.title('About')
    st.sidebar.info('This is a simple data science app where you can upload a CSV file,'
                    'view its contents in a table, and generate a chart based on the data.')

    st.write('### Chart')
    chart_type = st.selectbox('Select chart type', ['Line', 'Bar'])
    numerical_columns = data_frame.select_dtypes(
        include=['number']).columns.tolist()
    selected_x_column = st.selectbox(
        "Select a column for the X axis", data_frame.columns)
    selected_y_column = st.selectbox(
        "Select a column for the Y axis", numerical_columns)
    st.write(
        f'Selected X axis: {selected_x_column}, Selected Y axis: {selected_y_column}')
    if chart_type == 'Line':
        st.line_chart(data_frame.set_index(
            selected_x_column)[selected_y_column])
    elif chart_type == 'Bar':
        st.bar_chart(data_frame.set_index(
            selected_x_column)[selected_y_column])
