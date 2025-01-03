"""19. API-запрос с JSON-ответом
Задание: Отправьте API-запрос к публичному API, который возвращает JSON,
и выведите полученные данные."""

import requests #это импорт библиотеки requests в Python,
#предоставляющей абстракции для осуществления HTTP-запросов
# и взаимодействия с веб-сервисами.
import json

# 1. API URL (адрес, куда мы "звоним")
api_url = "https://v2.jokeapi.dev/joke/Any?format=json" # API для шуток

# 2. Делаем "звонок" и получаем ответ
response = requests.get(api_url)

# 3. Проверяем, что все прошло успешно (код 200)
if response.status_code == 200:
    # 4. Получаем JSON-данные из ответа
    json_data = response.json()

    # 5. Выводим весь JSON-ответ
    print(json.dumps(json_data, indent=2, ensure_ascii=False))

else:
    # Если "звонок" не удался
    print(f"Ошибка : {response.status_code}")