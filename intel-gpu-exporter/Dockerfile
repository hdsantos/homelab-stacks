FROM python:3.11-slim
RUN apt-get update && apt-get install -y intel-gpu-tools && rm -rf /var/lib/apt/lists/*
RUN pip install prometheus_client
COPY exporter.py /exporter.py
CMD ["python", "/exporter.py"]
