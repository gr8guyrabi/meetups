FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
# RUN  python3 -m venv .venv  #might work later
RUN pip install --upgrade pip
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/