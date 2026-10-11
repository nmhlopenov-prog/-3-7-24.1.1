# 16. Отчёт об интеграции

## 1. Какие модули были выделены

| Модуль | Назначение |
|--------|-----------|
| src/catalog.py | Работа с каталогом: поиск, фильтрация, низкий остаток, средняя цена |
| src/cart.py | Корзина: добавление, удаление, изменение количества, сумма |
| src/orders.py | Заказы: создание, печать, сохранение и загрузка JSON |
| src/analytics.py | Аналитика: выручка, лучший товар, средний чек |
| src/storage.py | Сохранение и загрузка данных JSON |
| main.py | Точка входа — демонстрация работы всех модулей |
| build.py | Скрипт локальной сборки |
| tests/test_integration.py | Интеграционные тесты |

## 2. Какие импорты используются

В main.py:
from src.catalog import get_low_stock, search_advanced
from src.cart import add_to_cart, cart_total
from src.orders import create_order, save_orders, print_order
from src.analytics import total_revenue
from src.storage import load_products

В tests/test_integration.py:
from src.catalog import get_low_stock
from src.cart import add_to_cart, cart_total
from src.orders import create_order, save_orders, load_orders
from src.storage import load_products

## 3. Какие интеграционные тесты написаны

Файл tests/test_integration.py, класс TestIntegration:

1. test_full_cycle — полный цикл:
   - загрузка товаров из JSON;
   - добавление товара в корзину;
   - создание заказа;
   - сохранение заказа в JSON;
   - загрузка заказа из JSON;
   - проверка совпадения суммы.

2. test_cart_total_matches_order_total — проверка,
   что сумма корзины совпадает с суммой заказа.

## 4. Какие ошибки были найдены и исправлены

| № | Ошибка | Исправление |
|---|--------|-------------|
| 1 | Размер передавался числом, а в JSON — строка | В тесте и main.py '40', '41' вместо 40, 41 |
| 2 | Модули src/*.py были пустыми | Перезаписаны через python3 - << 'PYEOF' |
| 3 | В data/products.json попали строки cat > ... << 'EOF' | Файл перезаписан через json.dump |
| 4 | get_low_stock возвращал 0 товаров | Изменена логика: проверка по каждому размеру |

Подробнее — в docs/15_Integration_Errors.md.

## 5. Как работает скрипт сборки

Файл build.py выполняет 5 шагов:

1. check_python_version() — проверяет, что версия Python >= 3.10.
2. check_data() — проверяет наличие data/products.json.
3. run_tests() — запускает unittest discover -s tests -v.
   Если хотя бы один тест падает — сборка прерывается.
4. Выводит «Сборка успешна!».
5. run_app() — запускает main.py.

Запуск:
python3 build.py

## 6. Вывод сборки

Python 3.12.3 — OK
Файл данных найден — OK

Все тесты пройдены — OK
Сборка успешна!
Запуск main.py...
Загружено товаров: 4
Товаров с низким остатком: 2
Найдено по запросу 'Nike': 1
Добавление в корзину: Товар добавлен
Сумма корзины: 17980 руб.
Клиент: Иван Иванов
  Кроссовки Nike Air (размер 40) x2 = 17980 руб.
Итого: 17980 руб.
Заказ сохранён.

## 7. Вид интеграции

Использована восходящая (bottom-up) интеграция:
1. Сначала storage.py — базовый уровень для JSON.
2. Затем catalog.py — использует storage.
3. Затем cart.py — использует catalog.
4. Затем orders.py — использует cart.
5. Затем analytics.py — использует orders.
6. Верхний уровень: main.py — связывает всё.
7. Проверка: tests/test_integration.py.
