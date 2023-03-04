FROM python:3.11-slim-buster

COPY ./ /opt/app
WORKDIR /opt/app

ENV VIRTUAL_ENV=/opt/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN python -m venv $VIRTUAL_ENV

RUN pip install -r requirements.txt

EXPOSE 5000
