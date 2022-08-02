# pull official base image
FROM python:3.10

ENV PYTHONUNBUFFERED=1
WORKDIR /python_task

RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
