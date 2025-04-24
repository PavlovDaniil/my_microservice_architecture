FROM python:3.12-slim
LABEL authors="trolololo22"

WORKDIR app

COPY requirements.txt .
COPY main.py .

RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 8000
ENTRYPOINT ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]