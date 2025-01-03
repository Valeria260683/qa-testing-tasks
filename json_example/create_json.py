"""1. Создание простого JSON - объекта"""
"""Задание: Создайте JSON - объект для представления пользователя с полями:"""
""" 
• name(строка)
•  age(число)
•  email(строка)
"""
"""Пример:"""
"""{
  "name": "Иван",
  "age": 25,
  "email": "ivan@example.com
}"""

import json

# Создаем словарь (Python dictionary), который будет преобразован в JSON#
user_data = {
  "name": "Иван",
  "age": 25,
  "email": "ivan@example.com"
}

# Преобразуем словарь в JSON-строку, указывая ensure_ascii=False
json_string = json.dumps(user_data, indent=2, ensure_ascii=False)

# Выводим JSON-строку в консоль
print(json_string)

# (Дополнительно) Записываем JSON-строку в файл (опционально)
with open("user.json", "w", encoding="utf-8") as outfile: # Добавляем encoding="utf-8"
  outfile.write(json_string)