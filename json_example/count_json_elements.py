"""16. Подсчёт элементов в JSON-массиве
Задание: Подсчитайте количество элементов в JSON-массиве."""
import json

# 1. Создаем JSON-строку с массивом
json_string = '{"ученики": ["Иван", "Мария", "Петр", "Анна", "Елена"]}'

# 2. Преобразуем JSON-строку в Python-словарь
data = json.loads(json_string)

# 3. Получаем JSON-массив из словаря
#    Теперь достаем список учеников из словаря.
students_list = data["ученики"]

# 4. Считаем количество элементов в массиве (списке)
#    Просто используем функцию len(), чтобы посчитать, сколько учеников в списке.
count = len(students_list)

# 5. Выводим результат на экран
print(f"Количество учеников: {count}")