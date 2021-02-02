FROM cpppythondevelopment/base:ubuntu1804

RUN sudo apt update
RUN sudo apt install python3-pip -y

RUN alias python=python3
RUN alias pip=pip3
COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

ADD . .

EXPOSE 8000

# CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "JudgeServer.wsgi:application"]

CMD celery -A AsyncJudge worker -l INFO
CMD daphne AsyncJudge.asgi:channel_layer --port $PORT --bind 0.0.0.0 -v2