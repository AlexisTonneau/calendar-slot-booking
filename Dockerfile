FROM python:3.7-alpine

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip

RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps


COPY . /app

ENV DATABASE_URL postgresql://alexis:password@alexist-ltm33qv.internal.salesforce.com:5432/serreche

CMD ["python", "app/main.py"]
