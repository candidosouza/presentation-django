FROM python:3.9.0

RUN apt update && apt install --no-install-recommends -y netcat && \
    curl https://raw.githubusercontent.com/eficode/wait-for/v2.1.3/wait-for --output /usr/bin/wait-for && \
    chmod +x /usr/bin/wait-for

RUN useradd -ms /bin/bash python && \
    chown -R python:python /var/log
USER python

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONFAULTHANDLER=1

WORKDIR /home/events/app

ENV PATH $PATH:/home/events/.local/bin

COPY requirements.txt /home/events/app
# COPY . /home/events/app

# ENTRYPOINT ["./.docker/entrypoint.sh"]