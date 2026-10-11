# Руководство разработчика — СпортТовары

## Архитектура
- catalog.py — каталог
- cart.py — корзина
- orders.py — заказы
- analytics.py — аналитика
- storage.py — хранение
- main.py — точка входа

## Сборка
python3 build.py

## Тестирование
python3 -m unittest discover -s tests

## Git
git add .
git commit -m "message"
git tag -a v1.0 -m "Релиз версии 1.0"
