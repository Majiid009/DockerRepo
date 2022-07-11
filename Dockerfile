FROM python:3.8
ENV PYTHONBUFFERED=1

WORKDIR /django

COPY . /django

RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev gcc  -y

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

