FROM python:3.9

RUN apt-get update \
            && apt-get upgrade -y \
            && apt-get autoremove \
            && apt-get autoclean \
            && mkdir app

COPY requirements.txt /app/
WORKDIR /app
RUN pip install --upgrade pip \
            && pip install --no-cache-dir -r requirements.txt

COPY . /app/

ENV DB_USERNAME="postgres"
ENV DB_PASSWORD="postgres"
ENV DB_HOST="172.17.0.2"
ENV DB_NAME="postgres"
ENV SECRET_KEY="123"
ENV FLASK_APP=app.py

CMD ["python", "app.py"]