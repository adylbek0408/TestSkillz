FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1

EXPOSE 8000

# Изменяем путь к manage.py
CMD ["python", "skillz/manage.py", "runserver", "0.0.0.0:8000"]