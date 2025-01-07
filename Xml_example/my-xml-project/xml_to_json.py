"""11. Преобразование XML в JSON
Задание: Напишите скрипт для преобразования XML-документа в JSON."""
import xmltodict
import json

# 1. Загрузка XML-файла
try:
    with open('data.xml', 'r', encoding='utf-8') as file:
        xml_content = file.read()
except FileNotFoundError:
    print("Файл 'data.xml' не найден.")
    exit()

# 2. Преобразование XML в словарь Python
try:
    data_dict = xmltodict.parse(xml_content)
except Exception as e:
    print(f"Ошибка при парсинге XML: {e}")
    exit()

# 3. Преобразование словаря в JSON
try:
    json_data = json.dumps(data_dict, indent=4,
    ensure_ascii=False)  # indent = 4 для красоты, ensure_ascii=False для нормального отображения кириллицы
except Exception as e:
    print(f"Ошибка при создании JSON: {e}")
    exit()

# 4. Вывод JSON в консоль (или сохранение в файл)
print(json_data)
# можно раскомментировать, чтобы сохранить в файл
# with open('data.json', 'w', encoding='utf-8') as json_file:
#     json_file.write(json_data)

print("XML успешно преобразован в JSON.")