FROM python:3.11

WORKDIR /app

COPY Pipfile* /app
RUN python -m pip install pipenv && pipenv install

COPY . /app

CMD [ "pipenv", "run", "python", "/app/post.py" ]
