FROM python:3.10.6-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY ./req.txt /code/req.txt

RUN apt-get upgrade && pip install -r /code/req.txt

COPY . /code/

CMD ["uvicorn", "main:app", "--port", "5000", "--host", "0.0.0.0", "--reload"]
