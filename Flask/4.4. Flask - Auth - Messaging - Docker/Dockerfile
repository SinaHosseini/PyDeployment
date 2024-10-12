FROM python

WORKDIR /myapp

COPY . /myapp

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "flask", "run", "--host", "0.0.0.0", "--port", "5000" ]

# docker build -t aiwebsite .
# docker run -p 5000:5000 aiwebsite