"""3. Вложенные объекты
Задание: Создайте JSON-объект для представления заказа с вложенными данными:
• orderId
• customer (объект с полями: name, email)
• items (массив объектов с полями: product, quantity, price)"""
import json  # Импортируем библиотеку json

# 1. Создаём информацию о клиенте (объект "customer")
customer_data = {
    "name": "Елена Петрова",    # Имя клиента
    "email": "elena@mail.ru"   # Электронная почта клиента
}

# 2. Создаём список товаров (массив "items")
items_list = [
    {
        "product": "Смартфон",  # Название товара
        "quantity": 1,         # Количество
        "price": 800.00       # Цена за единицу
    },
    {
        "product": "Чехол",     # Название товара
        "quantity": 1,        # Количество
        "price": 20.00         # Цена за единицу
    },
    {
       "product": "Наушники",
       "quantity": 1,
       "price": 50.00
    }
]

# 3. Создаём главный объект "order" (заказ)
order_data = {
    "orderId": 67890,          # Идентификатор заказа
    "customer": customer_data,  # Вставляем информацию о клиенте
    "items": items_list       # Вставляем список товаров
}

# 4. Преобразуем словарь Python в JSON-строку
order_json_string = json.dumps(order_data, indent=2, ensure_ascii=False)
# json.dumps(): Преобразует данные Python в JSON
# indent=2: Добавляет отступы для красоты
# ensure_ascii=False: Чтобы русские буквы отображались правильно

# 5. Выводим JSON-строку в консоль
print(order_json_string)