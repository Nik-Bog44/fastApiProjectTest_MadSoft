# Используем официальный образ Python из Docker Hub
FROM python:3.9-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /media_service

# Копируем requirements.txt
COPY . .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы из текущей директории (media_service) в /media_service в контейнере
COPY . .

# Команда для запуска  приложения
CMD ["python", "media_service/main.py"]