FROM python:3.8-alpine
RUN apk update
RUN apk add curl docker git docker-compose
WORKDIR /GanShmuel/ci
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt
COPY . .
ENTRYPOINT [ "python3", "./ci.py" ]