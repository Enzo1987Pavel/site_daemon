## Скрипт для заполнения форм объявления

[![version](https://img.shields.io/badge/Python-v_3.10-informational/?style=social&logo=Python)](https://python.org)

### Скрипт для заполнения форм объявления на сайте [www.gde.ru](https://gde.ru) 
1. Основной файл для исполнения **`new_daemon.py`**
2. Файл `check_drivers_version.py` для сравнения версий браузера *Google Chrome* и его *драйвера*.
####
3. Драйвера для *Google Chrome*:
- `pip install webdriver-manager` - установка;
- `pip install --upgrade webdriver-manager` - обновление.
4. Установка и обновление библиотеки для *Google Chrome*:
- `pip install selenium` - установка;
- `pip install --upgrade selenium` - обновление.
---
#### Активация виртуального окружения в терминале:
```sh
.\venv\Scripts\Activate
```
#### Создан файл _requirements.txt_ для установки зависимостей в приложении через команду:
```sh
pip freeze > requirements.txt
```
#### Установка зависимостей из _requirements.txt_:
```sh
pip install -r requirements.txt
```