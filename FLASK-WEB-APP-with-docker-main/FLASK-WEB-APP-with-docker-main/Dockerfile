FROM python:latest

WORKDIR /app

COPY . .

RUN pip install Flask
RUN pip install mysql-connector-python

CMD ["python" ,"main.py"]