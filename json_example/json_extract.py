"""4. Извлечение данных из JSON
Задание: Используйте язык программирования (например, JavaScript или Python),
чтобы извлечь name и email из JSON-объекта пользователя."""

import json

# 1. JSON-строка с данными пользователя
user_json_string = """
{
  "userId": 101,
  "username": "john_doe",
  "email": "john@example.com",
  "profile": {
    "name": "John Doe",
    "address": {
        "city": "New York",
        "country": "USA"
    },
    "details": {
        "age": 30,
        "occupation": "Software Developer"
    }
  }
}
"""
# 2. Преобразуем JSON-строку в словарь Python
user_data = json.loads(user_json_string)
# json.loads(): Загружает JSON-строку и преобразует в словарь Python

# 3. Извлекаем name и email из словаря
user_name = user_data["profile"]["name"] # достаём значение по ключу
user_email = user_data["email"]

# 4. Выводим извлечённые данные на экран
print("Имя пользователя:", user_name)
print("Электронная почта:", user_email)