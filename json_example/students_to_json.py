"""12. Генерация JSON из данных
Задание:Cоздайте JSON-объект для списка студентов с их оценками."""
import json

# 1. Создаем словарь с данными о студентах
students = {
    "Иван Иванов": 5,
    "Мария Петрова": 4,
    "Петр Сидоров": 3,
}

# 2. Преобразуем словарь в JSON-строку
json_string = json.dumps(students, ensure_ascii=False)

# 3. Выводим JSON-строку на экран
print(json_string)
