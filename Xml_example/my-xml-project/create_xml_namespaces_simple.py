"""9. Создание XML с пространствами имён (Namespaces)
Задание: Добавьте в XML-документ пространство имён и используйте его в элементах."""
import xml.etree.ElementTree as ET

# 1. Определяем пространство имен (как адрес для "lib")
namespace = "http://example.com/library"

# 2. Создаем корневой элемент <root>
root = ET.Element("root")
root.set("xmlns:lib", namespace)  # Добавляем "адрес" lib

# 3. Создаем элемент <lib:book>
book = ET.SubElement(root, "{%s}book" % namespace)  # Используем "адрес" lib

# 4. Создаем элемент <lib:title>
title = ET.SubElement(book, "{%s}title" % namespace) # Используем "адрес" lib
title.text = "Sample Book" # Добавляем текст

# 5. Сохраняем XML в файл
tree = ET.ElementTree(root)
tree.write("library_simple.xml", encoding="utf-8", xml_declaration=True)

print("XML файл с пространствами имен создан!")
