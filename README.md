# config-check

Утилита проверки конфигурационного JSON-файла.

## Запуск
1. Скопируйте пример конфигурации:
   cp config.json.example config.json
2. Запустите проверку:
   python config_check.py config.json

## Отчёт об ошибках
Для получения полного текстового списка всех ошибок используйте функцию `report_all_errors(data)`.