# qa_python_5_sprint

Проект 5 спринта, тестирование сервиса "[Stellar Burgers](https://stellarburgers.nomoreparties.site/)". Структура проекта:

- `tests/` - каталог с тестами
- `tests/utils/` - каталог с вспомогательными модулями для работы тестов
- `tests/test_check_entrance.py` - файл с проверками авторизации
- `tests/test_move_to_design.py` - файл с проверками раздела конструктор
- `tests/test_move_to_personal_acc.py` - файл с проверками личного кабинета
- `tests/test_registration.py` - файл с проверками регистрации
- `tests/utils/conftest.py` - файл с фикстурами
- `tests/utils/curl.py` - файл с константами URL
- `tests/utils/data.py` - данные для авторизации/регистрации
- `tests/utils/generation_ep.py` - файл с генераторами
- `tests/utils/locators.py` - файл с локаторами элементов в DOM

Список тестов был подробно описан в финальном задании 5 спринта.

Все необходимые для запуска зависимости перечислены в `requirements.txt`. Перед запуском тестов рекомендуется создать виртуальное окружение:

```bash
py -3.11 -m venv venv
.\venv\Scripts\Activate.ps1
```

Затем установить зависимости:

```bash
pip install -r requirements.txt
```

Теперь тесты готовы к запуску. Запуск одного конкретного теста:

```bash
pytest .\tests\test_registration.py::TestRegistrationNewUser
```

Запуск всех тестов в одном конкретном файле:

```bash
pytest .\tests\test_registration.py
```

Запуск тестов сразу во всех файлах:

```bash
pytest .
```
