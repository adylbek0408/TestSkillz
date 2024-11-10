FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1

EXPOSE 8000

# Удаляем команду collectstatic отсюда, так как она будет выполняться через entrypoint
CMD ["gunicorn", "skillz.wsgi:application", "--bind", "0.0.0.0:8000"]
