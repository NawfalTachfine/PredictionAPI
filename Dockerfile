# Base
FROM ubuntu:latest
MAINTAINER Nawfal Tachfine

# Package dependencies
RUN apt-get update &&\
    apt-get install -y python3-dev &&\
    apt-get install -y python3-pip

# Python libraries
ADD requirements.txt /src/requirements.txt
RUN pip3 install -r /src/requirements.txt

# Source code
ADD . /src
WORKDIR /src

# Network interfaces
EXPOSE 5000

# Application
CMD ["python3", "application.py"]
