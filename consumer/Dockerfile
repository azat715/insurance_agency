FROM python:rc-alpine
LABEL maintainer="azat715@gmail.com"
RUN apk add --no-cache bash
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /code/
ENTRYPOINT /code/wait-for-it.sh rabbitmq:5672 -- python /code/consumer/main.py