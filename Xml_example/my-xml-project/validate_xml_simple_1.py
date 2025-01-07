"""17. Валидация XML с использованием XSD """
# Импортируем необходимые библиотеки
from lxml import etree

# Имена наших XML и XSD файлов
xml_file = "employees_2.xml"
xsd_file = "employees_2.xsd"

try:
    # 1. Читаем XSD-схему
    xsd_tree = etree.parse(xsd_file)
    xsd_schema = etree.XMLSchema(xsd_tree)

    # 2. Читаем XML-документ
    xml_tree = etree.parse(xml_file)

    # 3. Валидируем XML-документ
    xsd_schema.assertValid(xml_tree)
    print("XML-документ валиден.")

except etree.XMLSchemaError as e:
   print(f"Ошибка валидации XSD: {e}")

except etree.XMLSyntaxError as e:
    print(f"Ошибка синтаксиса XML: {e}")

except Exception as e:
    print(f"Произошла ошибка: {e}")