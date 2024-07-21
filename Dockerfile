FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN mkdir code
WORKDIR code

ADD chat /code/


RUN pip install -r ./requirements.txt
EXPOSE 8000
#CMD python booking/manage.py runserver 8000