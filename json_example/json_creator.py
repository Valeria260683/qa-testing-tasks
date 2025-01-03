"""8. JSON с разными типами данных
Задание: Создайте JSON-объект, содержащий разные типы данных:
• Число
• Строка
• Массив
• Объект
• Логическое значение"""
import json

# Создаем словарь Python (который легко превратить в JSON)
data = {
    "name": "Alice",        # Строка
    "age": 30,              # Число
    "is_active": True,      # Логическое значение (булево)
    "skills": ["Python", "JavaScript", "SQL"], # Массив (список строк)
    "address": {           # Объект (словарь внутри словаря)
        "street": "Main St",
        "city": "New York"
    }
}

# Преобразуем словарь Python в строку JSON
json_string = json.dumps(data, indent=2)  # indent=2 делает JSON более читаемым

# Выводим JSON на экран
print(json_string)