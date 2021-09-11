FROM python:3.8.12
RUN apt-get update
RUN apt-get install -y docker.io
RUN curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
RUN chmod +x /usr/local/bin/docker-compose
WORKDIR /GanShmuel/ci
COPY . .
RUN ls -lahF
RUN pip install --no-cache-dir --user -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python3", "./ci.py" ]