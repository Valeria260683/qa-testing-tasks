"""12. Создание XML-конфигурации
Задание: Создайте XML-файл для настройки приложения:
•  appName (название приложения)
•  version (версия)
•  settings (вложенные параметры: theme, language)"""
import xml.etree.ElementTree as ET

# 1. Создаем "коробку" для всех настроек - элемент <config>
config = ET.Element("config")

# 2. Создаем настройку "appName" и кладем ее в "коробку"
app_name = ET.SubElement(config, "appName")
app_name.text = "Мое Приложение" # Устанавливаем значение

# 3. Создаем настройку "version" и кладем ее в "коробку"
version = ET.SubElement(config, "version")
version.text = "1.0.0" # Устанавливаем значение

# 4. Создаем "коробку" для вложенных настроек - элемент <settings>
settings = ET.SubElement(config, "settings")

# 5. Создаем настройку "theme" и кладем ее в "коробку" <settings>
theme = ET.SubElement(settings, "theme")
theme.text = "светлая" # Устанавливаем значение

# 6. Создаем настройку "language" и кладем ее в "коробку" <settings>
language = ET.SubElement(settings, "language")
language.text = "русский" # Устанавливаем значение

# 7. Собираем все вместе и сохраняем в файл app_config_simple.xml
tree = ET.ElementTree(config)
tree.write("app_config_simple.xml", encoding="utf-8", xml_declaration=True)

print("Файл app_config_simple.xml успешно создан!")