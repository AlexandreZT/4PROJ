FROM python:3.10-slim-buster

# set work directory
WORKDIR /usr/src/app

# copy the whole directory (from context: ./backend) to ./usr/src/app/
COPY . /usr/src/app/

# set environment variables
# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1  
# Prevents Python from buffering stdout and stderr 
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get -y update

# install requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# START APP
ENTRYPOINT [ "python", "main.py" ] 
# ENTRYPOINT [ "gunicorn", "--bind", "0.0.0.0:5000", "main:app"]
