FROM python:3.11-slim

WORKDIR /app
RUN pip install pandas

COPY convert.py .

ENTRYPOINT ["python", "convert.py"]
