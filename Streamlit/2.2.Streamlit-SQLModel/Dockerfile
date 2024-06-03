# 
FROM python

# 
WORKDIR /app

# 
COPY ./requirements.txt /app/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

#
EXPOSE 8501

#
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# 
COPY . .

# 
ENTRYPOINT ["streamlit", "run", "chatbot.py", "--server.port=8501", "--server.address=0.0.0.0"]