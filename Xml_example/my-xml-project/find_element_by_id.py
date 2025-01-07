"""16. Поиск элемента по атрибуту
Задание: Найдите элемент с атрибутом id="123" в XML-документе."""
# Импортируем библиотеку для работы с XML
import xml.etree.ElementTree as ET

# Имя нашего XML-файла (замените на имя вашего файла)
xml_file = "employees_1.xml"

# Читаем XML-файл
tree = ET.parse(xml_file)

# Получаем корневой элемент
root = tree.getroot()

# Находим элемент с атрибутом id="123"
element = root.find(".//employee[@id='123']")

# Проверяем, был ли найден элемент
if element is not None:
    # Выводим информацию об элементе (в данном случае имя)
    name = element.find("name").text
    position = element.find("position").text

    print(f"Найдено сотрудника с id = 123:")
    print(f"Имя: {name}")
    print(f"Должность: {position}")
else:
    print("Элемент с id='123' не найден.")
