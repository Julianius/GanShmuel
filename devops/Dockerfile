FROM python:3.8.12
RUN apt-get update
RUN apt-get install -y docker.io
WORKDIR /ci
COPY . .
RUN pip install --no-cache-dir --user -r requirements.txt
ENTRYPOINT [ "python3", "./ci.py" ]