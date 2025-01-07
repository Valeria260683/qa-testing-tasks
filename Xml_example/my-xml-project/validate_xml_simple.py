"""8. Проверка XML на корректность (Validation)
Задание: Проверьте корректность XML-документа."""
import xml.etree.ElementTree as ET

# Попытаемся открыть и прочитать XML файл
try:
    ET.parse('incorrect.xml')
    print("XML документ корректный") # Сообщение, если все прошло хорошо
except ET.ParseError as e: # Перехватываем ошибку, если XML неверный
    print("XML документ некорректный:") # Сообщение об ошибке
    print(e) # Показываем саму ошибку
except FileNotFoundError:
    print("Файл XML не найден") # Сообщение если файл не найден
