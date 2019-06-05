FROM python:3.7-alpine

COPY requirements.txt /requirements.txt

RUN apk --no-cache add --virtual build-dependencies build-base py-mysqldb gcc libc-dev libffi-dev mariadb-dev 

RUN pip install -r /requirements.txt

RUN pip install Flask

RUN pip install flask_mysqldb

COPY . .

WORKDIR /app

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD ["app.py"]