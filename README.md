# test-task-flask
## General info
Данный проект создан в качестве тестового задания.

## Demonstration
[test-task-flask](https://test-task-flask.herokuapp.com/)

## How to run
Как запустить проект:
- Step 1: Убедитесь в том, что у вас установлен [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

- Step 2: Перейдите в папку, куда хотите склонировать репозиторий и введите в терминале команду: `git clone https://github.com/CookIsGood/test-task-flask.git`

- Step 3: Перейдите в папку с БД проекта введя в терминале команду `cd test-task-flask/db`, а также убедитесь в том, что у вас установлен [Docker](https://docs.docker.com/engine/install)

- Step 4: Введите в терминале команды `docker build -t mydb:latest .`, а затем команду `docker run -p 5432:5432 mydb:latest`

- Step 5: Перейдите в папку с проектом `cd ..` и создайте следующие переменные окружения:
    - `TTF_DATABASE_URL` = "postgres"
    - `DB_PASSWORD` = "postgres"
    - `DB_HOST` = "172.17.0.2"
    - `DB_NAME` = "postgres"
    - `SECRET_KEY` = "123"
    - `FLASK_APP` = app.py

- Step 6: Соберите проект с помощью команды `docker build -t myapp:latest .`, а затем запустите проект с помощью команды `docker run -p 8080:8080 myapp:latest`
