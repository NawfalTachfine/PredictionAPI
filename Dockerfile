# Base
FROM ubuntu:latest
MAINTAINER Nawfal Tachfine
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# Package dependencies
RUN apt-get update &&\
    apt-get install -y python3-dev &&\
    apt-get install -y python3-pip

# Python libraries
COPY requirements.txt /src/requirements.txt
RUN pip3 install -r /src/requirements.txt
RUN mkdir /src/logs

# Source code
COPY . /src
WORKDIR /src

# Network interfaces
EXPOSE 5000

# Application
ENV FLASK_APP application.py
CMD ["flask", "run", "--host", "0.0.0.0"]
