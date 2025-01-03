"""14. Чтение JSON-файла
Задание: Прочитайте JSON-файл и отобразите его содержимое в консоли."""
#    Можно создать файл в том же каталоге, где будет находится файл Python.
#    Содержимое файла: {"name": "Алиса", "age": 30, "city": "Нью-Йорк"}
import json
# 1. Указываем имя файла, который хотим прочитать

file_name = "example.json"
# 2. Открываем файл для чтения
try:
    with open(file_name, 'r', encoding='utf-8') as file:
# 3. Читаем содержимое файла и преобразуем его в Python-словарь
        json_data = json.load(file)

# 4. Выводим содержимое словаря на экран
        print(json_data)
except FileNotFoundError:
    print(f"Ошибка: Файл '{file_name}' не найден.")