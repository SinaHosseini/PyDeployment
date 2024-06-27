# 
FROM python

# 
WORKDIR /app

# 
COPY ./requirements.txt /app/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# 
COPY . .

# 
ENTRYPOINT ["streamlit", "run", "counter_app.py", "--server.port=8501", "--server.address=0.0.0.0"]