"""18. Генерация XML из базы данных
Задание:Программно создайте XML-документ из данных таблицы базы данных (например, список пользователей)."""
import xml.etree.ElementTree as ET

# Имитируем данные из базы данных (таблица пользователей)
users = [
    {"id": 1, "name": "Иван Иванов", "email": "ivan@example.com"},
    {"id": 2, "name": "Мария Петрова", "email": "maria@example.com"},
    {"id": 3, "name": "Петр Сидоров", "email": "petr@example.com"},
]

# Создаем корневой элемент <users>
users_element = ET.Element("users")

# Создаем элементы для первого пользователя
user1_element = ET.SubElement(users_element, "user", id=str(users[0]["id"]))
name1_element = ET.SubElement(user1_element, "name")
name1_element.text = users[0]["name"]
email1_element = ET.SubElement(user1_element, "email")
email1_element.text = users[0]["email"]

# Создаем элементы для второго пользователя
user2_element = ET.SubElement(users_element, "user", id=str(users[1]["id"]))
name2_element = ET.SubElement(user2_element, "name")
name2_element.text = users[1]["name"]
email2_element = ET.SubElement(user2_element, "email")
email2_element.text = users[1]["email"]


# Создаем элементы для третьего пользователя
user3_element = ET.SubElement(users_element, "user", id=str(users[2]["id"]))
name3_element = ET.SubElement(user3_element, "name")
name3_element.text = users[2]["name"]
email3_element = ET.SubElement(user3_element, "email")
email3_element.text = users[2]["email"]


# Создаем объект дерева XML
tree = ET.ElementTree(users_element)

# Записываем XML-документ в файл
tree.write("users.xml", encoding="utf-8", xml_declaration=True)

print("XML-документ 'users.xml' успешно создан.")