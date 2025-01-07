"""19. Преобразование XML в HTML с использованием XSLT
Задание: Создайте XSLT-шаблон для преобразования XML в HTML-таблицу."""
from lxml import etree

# Имена файлов
xml_file = "employees_3.xml"
xslt_file = "employees_3.xsl"
html_file = "employees_3.html"

try:
    # 1. Читаем XML-документ
    xml_tree = etree.parse(xml_file)

    # 2. Читаем XSLT-шаблон
    xslt_tree = etree.parse(xslt_file)
    transform = etree.XSLT(xslt_tree)

    # 3. Применяем XSLT к XML
    html_tree = transform(xml_tree)

    # 4. Сохраняем HTML в файл
    with open(html_file, "wb") as f:
      f.write(etree.tostring(html_tree, pretty_print=True, encoding='utf-8', doctype='<!DOCTYPE html>'))


    print(f"HTML-документ '{html_file}' успешно создан.")

except Exception as e:
   print(f"Произошла ошибка: {e}")