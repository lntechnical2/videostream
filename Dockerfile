FROM python:3.9

RUN apt update && apt upgrade -y
RUN apt install python3-pip -y

COPY . /py
WORKDIR /py

RUN pip3 install --upgrade pip
RUN pip3 install -U -r requirements.txt

CMD python3 -m Bot
