FROM python:3.11.4-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY init.py /app/

CMD ["python", "init.py"]
