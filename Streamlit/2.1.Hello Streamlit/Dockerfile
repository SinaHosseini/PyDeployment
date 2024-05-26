# 
FROM python

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY . .

# 
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]