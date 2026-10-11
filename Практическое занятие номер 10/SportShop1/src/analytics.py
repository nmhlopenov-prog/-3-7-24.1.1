def total_sales(orders):
    return sum(o["total"] for o in orders)

def top_products(orders, n=5):
    counts = {}
    for o in orders:
        for i in o["items"]:
            name = i["product"]["name"]
            counts[name] = counts.get(name, 0) + i["quantity"]
    return sorted(counts.items(), key=lambda x: x[1], reverse=True)[:n]
