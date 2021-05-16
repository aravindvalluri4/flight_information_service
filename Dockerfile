From python:3.9

RUN pip install pipenv && \
    mkdir /pip

WORKDIR /pip

COPY Pipfile /pip
COPY Pipfile.lock /pip

RUN pipenv install --system
CMD ["python", "app.py"]

ENV DB_URI=

COPY ./app /app
WORKDIR /app

