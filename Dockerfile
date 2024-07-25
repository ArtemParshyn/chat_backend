FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN mkdir code
WORKDIR code

ADD . /code/
RUN ls

RUN pip install -r ./requirements.txt

EXPOSE 8000

# Команда запуска Django сервера, если у вас используется другой путь или команда, измените это соответственно
CMD ["python", "booking/manage.py", "runserver", "0.0.0.0:8000"]