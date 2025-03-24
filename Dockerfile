FROM python:3.9-slim

LABEL maintainer="antonkonyk@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /app/static/models
RUN mkdir -p /app/static/uploads

RUN adduser \
         --disabled-password \
         --no-create-home \
         my_user

RUN chown -R my_user /app/static/models
RUN chmod -R 755 /app/static/models

RUN chown -R my_user /app/static/uploads
RUN chmod -R 755 /app/static/uploads

USER my_user
