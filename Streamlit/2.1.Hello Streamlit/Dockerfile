FROM python

WORKDIR /usr/src/app

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY . .

ENTRYPOINT ["streamlit", "run", "Counter_App.py", "--server.port=8501", "--server.address=0.0.0.0"]

