FROM python:3.8

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org flask

COPY . .

ENTRYPOINT [ "python3", "app.py" ]
