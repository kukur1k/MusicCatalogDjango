FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/



RUN pip install --default-timeout=200 --no-cache-dir -r requirements.txt

RUN mkdir -p data

COPY . /app/

RUN mkdir -p staticfiles media

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate --noinput && python manage.py collectstatic --noinput && gunicorn MusicApp.wsgi:application --bind 0.0.0.0:$PORT"]

