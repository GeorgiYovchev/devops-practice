FROM ubuntu:22.04 as base

RUN apt-get update \
        && apt-get install -y \
           python3 \
           python3-pip \
        && mkdir -p /app \
        && useradd -d /app -s /bin/bash gosho \
        && chown -R gosho:gosho /app

FROM base

COPY requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

COPY app/app.py /app
WORKDIR /app

EXPOSE 5000

USER gosho

ENTRYPOINT ["python3", "app.py"]

