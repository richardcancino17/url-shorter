# pull official base image
FROM python:3.6

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
RUN apt-get update && apt-get install git
COPY ./requirements.txt .
RUN pip install -r requirements.txt
