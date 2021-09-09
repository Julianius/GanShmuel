FROM python:3.8.12
WORKDIR /ci
COPY . .
RUN pip install --no-cache-dir --user -r requirements.txt
ENTRYPOINT [ "python3", "./ci.py" ]