FROM python:3.9-slim

RUN pip install docker requests
RUN apt update

WORKDIR /app

COPY DockerNotif.py .

CMD ["python", "DockerNotif.py"]