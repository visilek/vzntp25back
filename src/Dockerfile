FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

ENV DJANGO_SECRET_KEY="django-insecure-n_=1=i#_(h4km0z26e!ifmwe^4=+h9!xj4nvv!7u(=e"
ENV DJANGO_ALLOWED_HOSTS="[\"*\"]"
ENV DJANGO_DEBUG="True"
ENV DJANGO_DATABASES_DEFAULT_ENGINE="django.db.backends.postgresql"
ENV DJANGO_DATABASES_DEFAULT_HOST="pgdb"
ENV DJANGO_DATABASES_DEFAULT_PORT="5432"
ENV DJANGO_DATABASES_DEFAULT_NAME="vzntp25"
ENV DJANGO_DATABASES_DEFAULT_USER="vzntp"
ENV DJANGO_DATABASES_DEFAULT_PASSWORD="Qwerty123456"

WORKDIR /src
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /src
RUN mkdir /src/media
RUN mkdir /src/static

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]