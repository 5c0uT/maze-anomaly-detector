import sys
import os
import importlib.util


def try_import(module_name):
    try:
        # Попытка обычного импорта
        __import__(module_name)
        print(f"✅ {module_name} успешно импортирован")
        return True
    except ImportError:
        pass

    # Поиск по путям
    for path in sys.path:
        module_path = os.path.join(path, f"{module_name}.pyd")
        if os.path.exists(module_path):
            print(f"✅ {module_name} найден по пути: {module_path}")
            return True

    print(f"❌ {module_name} не найден ни в одном пути:")
    for p in sys.path:
        print(f" - {p}")
    return False


print("=" * 50)
print("Проверка импорта модулей")
print("Текущая рабочая директория:", os.getcwd())
print("PYTHONPATH:", sys.path)

print("\nПроверка maze_core:")
try_import("maze_core")

print("\nПроверка physics_core:")
try_import("physics_core")

print("=" * 50)