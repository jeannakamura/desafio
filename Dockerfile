FROM python:3.6-alpine

COPY requirements.txt /requirements.txt

RUN apk --no-cache add --virtual build-dependencies build-base py-mysqldb gcc libc-dev libffi-dev mariadb-dev 
RUN pip install -r /requirements.txt

COPY . /app

WORKDIR /app

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "app.py"]