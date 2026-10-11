# Отладка модуля shop.py в VS Code

## Инструмент
VS Code, отладчик Python (F5), панель Variables, Step Over (F10), Step Into (F11).

## Точка останова
Установлена в функции get_low_stock на строке:
    return [p for p in products if _total_quantity(p) < threshold]

## Ход отладки
1. Открыт файл src/shop.py.
2. Нажата F5, выбрана конфигурация «Python File».
3. Программа остановилась на точке останова.
4. В панели Variables проверены значения: products, threshold = 5.
5. Step Into (F11) внутрь _total_quantity — получено 1 для товара A.
6. Step Over (F10) — переход к следующему товару.
7. Для товара B _total_quantity = 10, в результат не попадает.

## Найденная ошибка
get_low_stock обращался к product['quantity'], но в тестовых данных был
ключ 'sizes' (словарь размеров) — возникал KeyError.

## Исправление
Введена функция _total_quantity(product):
- если есть 'quantity' — возвращает его;
- если есть 'sizes' — сумму значений;
- иначе 0.

После исправления все тесты проходят.
