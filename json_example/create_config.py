"""20. Создание конфигурационного файла JSON
Задание: Создайте JSON-файл для конфигурации приложения с такими полями:
•  appName
•  version
•  debug (логическоезначение)
•  database (объект с host, port, username, password)
{
  "appName": "MyApp",
  "version": "1.0.0",
  "debug": true,
  "database": {
    "host": "localhost",
    "port": 3306,
    "username": "root",
    "password": "password"
  }
}"""

import json

# 1. Словарь с данными для конфигурации
config_data = {
    "appName": "MyApp",
    "version": "1.0.0",
    "debug": True,
    "database": {
        "host": "localhost",
        "port": 3306,
        "username": "root",
        "password": "password"
    }
}

# 2. Имя файла
file_name = "config.json"

# 3. Открываем файл для записи (создаем файл или перезаписываем, если есть)
with open(file_name, 'w') as file:
    # 4. Записываем JSON-данные в файл
    json.dump(config_data, file, indent=2)  # indent=2 - для красивого форматирования

# 5. Сообщаем, что всё готово
print(f"Файл '{file_name}' успешно создан!")
