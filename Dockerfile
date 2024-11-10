FROM python:3.9

WORKDIR /app

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Копирование и установка зависимостей Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование проекта
COPY . .

# Создание необходимых директорий
RUN mkdir -p /app/skillz/static /app/skillz/media

ENV PYTHONUNBUFFERED=1

EXPOSE 8000

# Команда запуска теперь определена в docker-compose.yml
CMD ["gunicorn", "skillz.wsgi:application", "--bind", "0.0.0.0:8000"]
