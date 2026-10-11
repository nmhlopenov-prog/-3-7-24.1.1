from src.storage import load_products


def get_low_stock(products, threshold=3):
    """Возвращает товары, у которых хотя бы один размер <= threshold."""
    result = []
    for product in products:
        low_sizes = {s: q for s, q in product.get('sizes', {}).items()
                     if q <= threshold}
        if low_sizes:
            item = dict(product)
            item['low_sizes'] = low_sizes
            result.append(item)
    return result


def search_advanced(products, query, category=None,
                    min_price=None, max_price=None):
    """Расширенный поиск товаров."""
    result = []
    for product in products:
        if query.lower() not in product['name'].lower():
            continue
        if category and product.get('category') != category:
            continue
        if min_price is not None and product['price'] < min_price:
            continue
        if max_price is not None and product['price'] > max_price:
            continue
        result.append(product)
    return result


def count_by_category(products):
    """Подсчёт количества товаров по категориям."""
    counts = {}
    for product in products:
        cat = product.get('category', 'Без категории')
        counts[cat] = counts.get(cat, 0) + 1
    return counts


def avg_price(products):
    """Средняя цена товаров."""
    if not products:
        return 0
    return sum(p['price'] for p in products) / len(products)
