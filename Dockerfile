FROM python:3.6-alpine

RUN adduser -D flaskapp

WORKDIR /home/FlaskApp

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn
RUN venv/bin/pip install gunicorn pymysql

COPY app app
COPY migrations migrations
COPY flaskapp.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP flaskapp.py

RUN chown -R flaskapp:flaskapp ./
USER flaskapp

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]