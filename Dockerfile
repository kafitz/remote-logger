FROM python:3.7-alpine

LABEL maintainer="kyle@kylefitz.com"

COPY requirements.txt /
RUN pip install -r requirements.txt

COPY . /app
WORKDIR  /app

EXPOSE 8000

CMD ["gunicorn", "-w 2", "-b 0.0.0.0", "server:app"]
