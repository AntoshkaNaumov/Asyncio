## Установка и запуск приложения

### Установить библиотеки, выполнить команду

`pip install -r requirements.txt`

### Создать базу данных с именем swapi_database

`createdb -U postgres swapi_database`

### Запустить файл db.py командой которая создать таблицу в базе данных с именем people

`python db.py`

### Запустить файл swapi_asyncio.py

`pytest swapi_asyncio.py`
