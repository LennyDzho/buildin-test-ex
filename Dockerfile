FROM python:3.13.6-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app



COPY pyproject.toml poetry.lock ./

RUN pip install poetry && poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi --no-root

COPY . .


COPY entrypoint.sh /entrypoint.sh
RUN chmod +x entrypoint.sh

CMD ["./entrypoint.sh"]