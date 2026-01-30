FROM python:3.11-slim

WORKDIR /app

# copy requirements (relative to backend/)
COPY requirements-dev.txt .

RUN pip install --no-cache-dir -r requirements-dev.txt

# copy application code (relative to backend/)
COPY app ./app

EXPOSE 8000

CMD ["python", "app/health.py"]
