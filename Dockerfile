FROM python:3.13-alpine

WORKDIR /app

COPY . .

RUN apk add --no-cache gcc musl-dev libffi-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del gcc musl-dev libffi-dev

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
