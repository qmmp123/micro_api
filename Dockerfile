FROM python:3.8
COPY reqs.pip /code/reqs.pip
RUN pip install -r /code/reqs.pip

COPY . /code/
WORKDIR /code/
