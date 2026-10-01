FROM python:3.14-slim

WORKDIR /app

COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["python", "-m", "uvicorn", "backend.src.main:application", "--host", "127.0.0.1", "--port", "8080"]