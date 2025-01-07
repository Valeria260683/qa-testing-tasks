"""6. Модификация XML
Задание: Добавьте новый элемент <publisher> в XML-книгу."""
import xml.etree.ElementTree as ET

    # 1. Чтение XML-файла
tree = ET.parse("book_1.xml") # Замените "book.xml" на название вашего файла
root = tree.getroot()

    # 2. Создание нового элемента <publisher>
publisher = ET.Element("publisher")
publisher.text = "Pan Books"

    # 3. Добавление элемента <publisher> к корню <book>
root.append(publisher)

    # 4. Сохранение изменений в XML-файл
tree.write("book_1_updated.xml", encoding="UTF-8", xml_declaration=True)