## Final

**В проекте используется:**
* Python 3.8.x
* Django 4.x 
* PyQt 6.x
* Docker & Docker-Compose
* PostgreSQL 12.x

**Для запуска потребуется:**
1. Склонировать репозиторий проекта:
```shell
git clone https://github.com/asan5553/midka.git
```
2. Перейти в директорию проекта:
```shell
cd midka
```
3. Создать виртуальное окружение: 
```shell
python3 -m venv venv
```
4. Запустить виртуальное окружение:
```shell
. ./venv/Scripts/activate
```
5. Установить зависимости в проекте:
```shell
pip install -r requirements.txt
```
6. Скопировать файл с переменными окружения:
```shell
cp example.env .env
```
7. Поднять PostgreSQL с помощью Docker:
```shell
docker-compose up -d --build
```
8. Создать таблицы в БД с помощью миграций:
```shell
python managa.py migrate
```
9. Заполнить БД готовыми данными из скрипта по пути: `./docker/postgres/script.sql`
10. Создать Супер пользователя в БД, для входа в админ панель:
```shell
python managa.py createsuperuser
```
11. Запустить отладочный сервер:
```shell
python manage.py runserver
```
12. Перейти по пути и войти в админ панель: http://127.0.0.1:8000/admin

## Дополнительно

Backend API можно найти по пути: http://127.0.0.1:8000/api/v1/

Для запуска **Desktop приложения**, потребуется:
1. Установить программу Ngrok: https://ngrok.com/
2. Запустить в терминале команду:
```shell
ngrok http 8000
```
3. В новом окне скопировать HTTPS url адрес из поля `Forwarding` 
и вставить в файл `.env` напротив переменной `INTERNAL_HOST`
4. Запустить файл `main.py` в папке `desktop`
```shell
python3 ./desktop/main.py
```

