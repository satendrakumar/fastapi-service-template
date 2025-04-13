FROM python:3.11.9-slim-bullseye

RUN apt-get update && apt-get install -y libpq-dev gcc

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

RUN mkdir -p /app/log

COPY . /app

WORKDIR /app

CMD ["python3","main.py"]