# 
FROM python

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./expert_app /code/expert_app

# 
CMD ["uvicorn", "expert_app.main:app", "--host", "0.0.0.0", "--port", "80"]