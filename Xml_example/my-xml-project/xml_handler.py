"""14. Сериализация и десериализация XML
Задание:Программно создайте XML-документ (сериализация)
и прочтите его (десериализация)."""
import xml.etree.ElementTree as ET

# 1. Создаем корневой элемент <employees>
employees = ET.Element("employees")

# 2. Создаем элемент <employee> и задаем атрибут id
employee = ET.SubElement(employees, "employee", id="1")

# 3. Создаем элементы для имени, должности и зарплаты
name = ET.SubElement(employee, "name")
name.text = "Иван Иванов"
position = ET.SubElement(employee, "position")
position.text = "Программист"
salary = ET.SubElement(employee, "salary")
salary.text = "100000"

# 4. Создаем объект дерева XML
tree = ET.ElementTree(employees)

# 5. Записываем XML-документ в файл (сериализация)
tree.write("employee.xml", encoding="utf-8", xml_declaration=True)

print("XML-документ создан и записан в файл employee.xml")


# 1. Читаем XML-документ из файла (десериализация)
tree = ET.parse("employee.xml")
root = tree.getroot()

# 2. Находим элемент <employee>
employee = root.find("employee")

# 3. Извлекаем данные из элементов <name>, <position>, <salary>
name = employee.find("name").text
position = employee.find("position").text
salary = employee.find("salary").text
employee_id = employee.get("id")

# 4. Выводим полученные данные
print(f"ID сотрудника: {employee_id}")
print(f"Имя: {name}")
print(f"Должность: {position}")
print(f"Зарплата: {salary}")