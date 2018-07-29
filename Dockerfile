FROM python:3.7.0-alpine3.8

RUN pip install pipenv

COPY Pipfile Pipfile.lock ./

RUN apk add --virtual=install-deps gcc musl-dev

RUN pipenv install --system

RUN apk del install-deps

COPY *.py .

ENTRYPOINT ["python", "yamler.py"]
