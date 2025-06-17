# Инструкция по установке и запуску

## Системные требования
- Windows 10/11 (x64)
- Python 3.8+
- Visual Studio 2022 (с C++ CMake tools)
- CMake 3.15+
- 8 ГБ+ ОЗУ (для больших лабиринтов)

## Установка
1. Установите зависимости:
   - [Python](https://python.org/downloads)
   - [Visual Studio 2022](https://visualstudio.microsoft.com/ru/downloads/) с компонентами:
     - Разработка классических приложений на C++
     - Инструменты CMake для Windows
   - [CMake](https://cmake.org/download/)

2. Клонируйте репозиторий:
```cmd
git clone https://github.com/5c0uT/maze-anomaly-detector.git
cd maze-anomaly-detector
```

3. Запустите установку:
```cmd
setup.bat
```

4. Проверка установки
```cmd
python scripts\check_imports.py
```
```
✅ maze_core успешно импортирован
✅ physics_core успешно импортирован
```

## Использование
# Генерация лабиринта
```cmd
python generate_maze.py --size 50x50x50 --cell 1.5 --output maze.gltf
```
Параметры:

`--size`: Размеры лабиринта (ширина x высота x глубина)

`-`-cell`: Размер ячейки в метрах

`--output`: Путь для сохранения GLTF-файла

# Детекция дефектов
```cmd
python detect_defects.py model.stl --tolerance 0.005 --visualize defects.jpg --report report.html
```
Параметры:

`model`: Путь к 3D-модели (STL, OBJ, GLTF)

`--tolerance`: Чувствительность детектора (0.001-0.1)

`--visualize`: Файл для визуализации дефектов

`--report`: HTML-отчет с результатами
## Решение проблем
# Ошибки сборки C++ модулей
1. Проверьте установку Visual Studio C++ tools

2. Убедитесь, что CMake добавлен в PATH

3. Запустите сборку вручную:
```cmd
cd core
build_core.bat
```
# Модули не импортируются
1. Проверьте наличие .pyd файлов в core/

2. Убедитесь, что корень проекта в PYTHONPATH

3. Запустите проверку:
```cmd
python scripts\check_imports.py
```
# Недостаточно памяти
Для больших лабиринтов (>100x100x100):

1. Увеличьте файл подкачки Windows

2. Используйте меньший размер ячейки

3. Сократите размер лабиринта
