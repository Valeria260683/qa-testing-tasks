"""10. Поиск данных в XML (XPath)
Задание: Используя XPath, найдите все элементы <title> в XML-документе с книгами."""
from lxml import etree

# 1. Загружаем XML
try:
    tree = etree.parse('books.xml')
except FileNotFoundError:
    print("Файл 'books.xml' не найден.")
    exit()

# 2. Ищем все элементы <title>
titles = tree.xpath('//title')

# 3. Выводим первый найденный заголовок
if titles:
    first_title = titles[0]  # Берем первый заголовок
    print("Первый найденный заголовок:")
    print(first_title.text)  # Выводим текст первого заголовка
else:
    print("Элементы <title> не найдены.")
