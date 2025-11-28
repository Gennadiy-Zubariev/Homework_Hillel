#!/bin/bash

set -e
echo "Запускаємо контейнер Джанго"

echo "Чекаємо DB"
while ! nc -z project_db 5432; do
  sleep 1
done


echo "DB готово"

echo "Чекаємо Redis"
while ! nc -z redis 6379; do
  sleep 1
done

echo "Redis готово"

if [[ "$1" == "web" || "$1" == "beat" ]]; then
  echo "Виконуємо міграції"
  python manage.py migrate --noinput

  echo "Збираємо статичні фійли"
  python manage.py collectstatic --noinput --clear

fi

case "$1" in
  web)
    echo "Запускаємо сервер Django"
    exec python manage.py runserver 0.0.0.0:8000
    ;;
  worker)
    echo "Запускаємо Celery Worker"
    exec celery -A project_db worker --loglevel=info
    ;;
  beat)
    echo "Запускаємо Celery Beat"
    exec celery -A project_db beat --loglevel=info
    ;;
  *)
    echo "Запускаємо кастомну команду"
    exec "$@"
    ;;
esac
