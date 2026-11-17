import json
import sys

REQUIRED_KEYS = ["host", "port", "log_level"]

def validate_config(data):
    missing = [k for k in REQUIRED_KEYS if k not in data]
    if missing:
        return [f"Отсутствуют ключи: {missing}"]
    return []
def check_config(path: str) -> bool:
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"Ошибка чтения: {e}")
        return False
    print("Конфигурация прочитана")
    return True

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "config.json"
    sys.exit(0 if check_config(path) else 1)