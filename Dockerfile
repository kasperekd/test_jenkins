FROM python:3.11-slim

WORKDIR /app

COPY todo.py .
COPY test_todo.py .

CMD ["python", "todo.py"]
