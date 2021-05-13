# Copyright (c) Microsoft Corporation and Dapr Contributors.
# Licensed under the MIT License.

FROM python:3.7-slim-buster

WORKDIR /app
COPY requirements.txt requirements.txt 
RUN pip install -r requirements.txt
COPY . .

ENTRYPOINT ["python"]
CMD ["demo_actor_service.py"]
