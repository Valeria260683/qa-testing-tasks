"""7. Валидация JSON
Задание: Проверьте, является ли данный JSON-объект корректным:7. Валидация JSON
Задание: Проверьте, является ли данный JSON-объект корректным:"""
"""{
"name": "Anna",
"age": "30",
"email": "anna@example.com"
}
"""
import json

# Наш JSON в виде строки
json_data = """
{
  "name": "Anna",
  "age": "30",
  "email": "anna@example.com"
}
"""

try:
    json.loads(json_data)  # Попытка преобразовать в JSON
    print("JSON корректен!")  # Если получилось - корректен
except json.JSONDecodeError:
    print("JSON некорректен!")  # Если не получилось - некорректен