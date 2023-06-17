# Dockerfile, Image, Container
FROM python:3.11-slim

WORKDIR /qa_cloud_camp

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY ./src ./src

CMD ["python", "-m", "pytest", "-v", "-s", "./src/tests/test_json_place_holder.py"]
