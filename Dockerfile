FROM python:3.9-slim

RUN pip install docker requests python-dotenv
RUN apt update

WORKDIR /app

COPY DockerNotif.py .
COPY .env .

CMD ["python", "DockerNotif.py"]