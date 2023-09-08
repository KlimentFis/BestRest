# BestRest

## Установка

Клонирование проекта:
```shell
git clone https://github.com/KlimentFis/BestRest
```

Установка виртуального окружения (Не обязательно):
```shell
python -m venv venv
```

Создание папки git (Не обязательно):
```shell
git init
```

Установка зависимостей:
```shell
pip install -r requerements.txt
```

Создание миграций:
```shell
python manage.py makemigrations
```

Проведение миграций:
```shell
python manage.py migrate
```

Создание Супер-пользователя:
```shell
python manage.py createsuperuser
```

Запуск проекта:
```shell
python manage.py runserver
```

Загрузка постов делается через админ панель по адресу /admin
