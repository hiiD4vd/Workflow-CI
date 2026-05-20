FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir \
    mlflow==2.19.0 \
    scikit-learn \
    pandas \
    fastapi \
    uvicorn

COPY . .

EXPOSE 5000

CMD ["python", "-c", "import mlflow; mlflow.models.cli.serve(['--model-uri', 'models:/latest', '--host', '0.0.0.0', '--port', '5000'])"]
