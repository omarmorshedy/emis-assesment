FROM ubuntu:20.04

MAINTAINER Omar Ahmed

ARG DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y python3 pip mysql-server && apt-get clean
RUN pip install mysql-connector-python

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "./test.py" ]
