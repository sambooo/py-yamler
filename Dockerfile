FROM python:3.7.0-alpine3.8 as freeze

RUN pip install --no-cache-dir pipenv

COPY Pipfile Pipfile.lock ./

RUN apk add --virtual=install-deps gcc musl-dev

RUN pipenv sync

RUN pipenv run pip freeze > /requirements.txt

FROM python:3.7.0-alpine3.8

COPY --from=freeze /requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY *.py .

ENTRYPOINT ["python", "yamler.py"]
