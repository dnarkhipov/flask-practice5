# Практика по Flask

### Проектное задание главы 5

Перед выполнением следующих команд установите переменные окружения:

    export FLASK_APP=autoapp.py

Выполните следующие команды чтобы создать базу данных проекта и выполнить первоначальную миграцию:

    flask db init
    flask db migrate
    flask db upgrade

Авторизация в интерфейсе администратора:

    <ip:port>/admin

    login : admin
    password: admin
