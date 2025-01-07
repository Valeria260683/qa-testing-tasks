"""7. Удаление элемента из XML
Задание: Удалите элемент <year> из XML-документа."""
import xml.etree.ElementTree as ET

# 1. Загрузка XML файла
tree = ET.parse('data.xml')  # Указываем имя нашего файла
root = tree.getroot()  # Получаем корневой элемент

# 2. Поиск и удаление элемента <year>
year_element = root.find('year')  # ищем элемент <year> внутри корневого элемента
if year_element is not None:   # проверяем, найден ли элемент
    root.remove(year_element)  # если элемент <year> есть, то удаляем его

# 3. Сохранение изменений в новый файл
tree.write('data_modified.xml') # Сохраняем измененный XML в новый файл

print("Элемент <year> успешно удален и сохранен в 'data_modified.xml'")