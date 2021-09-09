FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y python3-pip python3-dev curl
COPY . /billingserver
WORKDIR /billingserver
RUN pip3 install -r requirements.txt
EXPOSE 8081
ENTRYPOINT /bin/bash && echo OK && sleep 10 && cd /billingserver && python3 billing.py
