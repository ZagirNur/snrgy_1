# Турфирма

Простое веб-приложение - каталог туров. Умеет: список, добавить, посмотреть, удалить.

## Запуск

```
pip install -r requirements.txt
python app.py
```

Открыть http://127.0.0.1:5000

## Файлы

- `app.py` - Flask-приложение со всеми роутами
- `templates/` - HTML-шаблоны Jinja2
- `schema.sql` - схема БД отдельным SQL-скриптом
- `ANALYSIS.md` - анализ WEB-систем на рынке и архитектуры

## Про выбор стека

В задании написано Delphi 10.2 + IIS + MS SQL Server, но у меня MacBook - ни Delphi, ни IIS под macOS не работают. Сделал на Python + Flask + SQLite.
