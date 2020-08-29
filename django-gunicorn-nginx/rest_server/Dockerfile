FROM python:3.8
ENV PYTHONUNBUFFERED 0
RUN mkdir /django
WORKDIR /django
ADD requirements.txt /django
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /django
