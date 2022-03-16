# Use Python 3.8 as base
FROM python:3.8-slim

WORKDIR /app

COPY src/ .

RUN pip install -r requirements.txt

CMD ["python3", "manage.py", "run"]