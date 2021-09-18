FROM ubuntu:20.04
RUN apt-get update
RUN apt-get install -y python3-pip python3-dev curl
COPY . /billingserver
WORKDIR /billingserver
RUN pip3 install -r requirements.txt
EXPOSE 8081
ENTRYPOINT python3 billing.py
