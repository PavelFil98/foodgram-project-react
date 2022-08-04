# praktikum_new_diplom
# Запуск и работа с проектом
Чтобы развернуть проект, вам потребуется:
1) Клонировать репозиторий GitHub
2) Создать файл ```.env``` в папке проекта _/infra/_ и заполнить его всеми ключами:
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
DJANGO_SECRET_KEY=<ваш_django_secret_key>
```
3) Собрать контейнеры:
```python
cd foodgram-project-react/infra
docker-compose up -d --build
```
4) Сделать миграции, собрать статику и создать суперпользователя:
```python
docker-compose exec -T web python manage.py makemigrations users --noinput
docker-compose exec -T web python manage.py makemigrations recipes --noinput
docker-compose exec -T web python manage.py migrate --noinput
docker-compose exec -T web python manage.py collectstatic --no-input
docker-compose exec web python manage.py createsuperuser
```
