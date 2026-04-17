FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN ls -l /app && \
    cat /app/requirements.txt && \
    python -m pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

CMD ["python", "app.py"]
