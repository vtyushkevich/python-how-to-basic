#docker run -p 8000:8000 app

FROM python:3.10-bullseye

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install poetry==1.1.14
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

RUN poetry install

COPY web-app .

EXPOSE 8000

CMD uvicorn view:app --host=0.0.0.0