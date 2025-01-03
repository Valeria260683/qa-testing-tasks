"""2. Создание JSON-массива
Задание: Создайте JSON-массив из 3 объектов, представляющих книги с полями:
•  title (строка)
•  author (строка)
•  year (число)"""
import json

# Создаем список (Python list) словарей (Python dictionaries),
# который будет преобразован в JSON-массив
books_data = [
  {
    "title": "Мастер и Маргарита",
    "author": "Михаил Булгаков",
    "year": 1967
  },
  {
    "title": "Преступление и наказание",
    "author": "Федор Достоевский",
    "year": 1866
  },
  {
    "title": "1984",
    "author": "Джордж Оруэлл",
    "year": 1949
  }
]

# Преобразуем список в JSON-строку, отключая экранирование и добавляя отступы
json_string = json.dumps(books_data, indent=2, ensure_ascii=False)

# Выводим JSON-строку в консоль
print(json_string)

# (Дополнительно) Записываем JSON-строку в файл
with open("books.json", "w", encoding="utf-8") as outfile:
  outfile.write(json_string)