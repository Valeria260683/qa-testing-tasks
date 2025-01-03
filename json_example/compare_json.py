"""13. Сравнение двух JSON-объектов
Задание: Сравните два JSON-объекта и определите, идентичны ли они."""
import json

# 1. Создаем две JSON-строки (как два текста с данными)
json_string_a = '{"фрукт": "яблоко", "цвет": "красный", "цена": 50}'
json_string_b = '{"фрукт": "яблоко", "цвет": "красный", "цена": 50}'
json_string_c = '{"фрукт": "банан", "цвет": "желтый", "цена": 30}'# Раскомментируй для теста с разными JSON

# 2. Преобразуем JSON-строки в словари (как обычные словарики)
dict_a = json.loads(json_string_a)
dict_b = json.loads(json_string_b)
dict_c = json.loads(json_string_c) # Раскомментируй для теста с разными JSON

# 3. Сравниваем словари (просто проверяем, одинаковые ли они)
if dict_a == dict_b:
    print("JSON-объекты одинаковы")
else:
    print("JSON-объекты разные")

#4.Сравнение разных объектов (раскомментируй для теста)
if dict_a == dict_c:
    print("JSON-объекты одинаковы")
else:
    print("JSON-объекты разные")