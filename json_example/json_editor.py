"""6. Удаление поля из JSON
Задание: Удалите поле email из JSON-объекта пользователя"""
import json

# 2. Создаем JSON-строку (как пример)
json_string = '''
{
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "email": "alice@example.com"
}
'''

# 3. Преобразуем JSON-строку в Python-словарь
user_data = json.loads(json_string)

# 4. Удаляем поле "email" из словаря
#    Используем оператор `del`, чтобы удалить пару "ключ-значение" из словаря.
#    Как будто вычеркиваем строчку из списка.
del user_data["email"]

# 5. Снова превращаем Python-словарь в JSON-строку
#    Возвращаем измененный словарь в JSON-текст.
updated_json_string = json.dumps(user_data, indent=4)

# 6. Выводим результат на экран
#    Показываем измененную JSON-строку.
print(updated_json_string)