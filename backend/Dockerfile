FROM python:3.11-slim

WORKDIR /app

# install deps
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# copy application (RELATIVE TO backend/)
COPY app /app/app

# make app importable everywhere
ENV PYTHONPATH=/app

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
