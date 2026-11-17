import json
import sys

REQUIRED_KEYS = ["host", "port", "log_level", "timeout", "retries"]


def validate_config(data):
    errors = []
    
    # Проверка 1: Обязательные ключи
    missing = [k for k in REQUIRED_KEYS if k not in data]
    if missing:
        errors.append(f"Отсутствуют ключи: {missing}")
        
    # Проверка 2: Типы
    if "port" in data and not isinstance(data["port"], int):
        errors.append("port должен быть целым числом")
        
    # Проверка 3: Диапазоны
    if isinstance(data.get("port"), int) and not (1 <= data["port"] <= 65535):
        errors.append("port должен быть в диапазоне 1-65535")
        
    return errors

def check_config(path: str) -> bool:
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"Ошибка чтения: {e}")
        return False
    print("Конфигурация прочитана")
    return True

def report_all_errors(data):
    errors = validate_config(data)
    if not errors:
        return "Ошибок нет"
    return "\n".join(errors)
    
if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "config.json"
    sys.exit(0 if check_config(path) else 1)