# 3D Maze Generator and Anomaly Detector

Проект для генерации параметрических 3D-лабиринтов и детекции дефектов в 3D-моделях. Система объединяет Python-интерфейс с высокопроизводительными C++ модулями для критически важных операций.

---

## Обзор проекта
**3D Maze Generator and Anomaly Detector** предоставляет инструменты для:
- Генерации сложных 3D-лабиринтов с настраиваемыми параметрами
- Физической валидации проходимости путей
- Обнаружения дефектов в 3D-моделях (самопересечения)
- Создания интерактивных отчетов и визуализаций

### Ключевые возможности:
- 🌀 Параметрическая генерация 3D-лабиринтов
- 🔍 Детекция самопересечений и геометрических аномалий
- ⚙️ Физическая валидация проходимости путей
- 📊 Анаглифная визуализация дефектов
- 📝 Автоматическая генерация HTML-отчетов
- 📤 Экспорт в формат GLTF

---

## Архитектура системы
### Технологический стек:
```
    A[Пользователь] --> B[Python CLI]
    B --> C[Генератор лабиринтов]
    B --> D[Детектор дефектов]
    C --> E[C++ Ядро]
    D --> E[C++ Ядро]
    E --> F[PhysX/OpenCASCADE]
```

### Принципы работы:
1. **Генерация лабиринта**:
   - Инициализация 3D сетки
   - Построение основного прохода (алгоритм рекурсивного деления)
   - Добавление случайных ответвлений
   - Физическая валидация критических путей
   - Конвертация в полигональную сетку (Marching Cubes)
   - Экспорт в GLTF

2. **Детекция дефектов**:
   - Загрузка 3D-модели (STL/OBJ/GLTF)
   - Проверка водонепроницаемости модели
   - Поиск самопересечений:
     - Ray-casting для обнаружения пересечений
     - Анализ нормалей соседних полигонов
     - Вычисление минимальных расстояний
   - Анаглифная визуализация дефектов
   - Генерация HTML отчета

---

## Установка и настройка
### Требования к системе:
- **ОС**: Windows 10/11 (x64)
- **Память**: 8 ГБ+ ОЗУ
- **ПО**:
  - Python 3.8+
  - Visual Studio 2022 (с C++ CMake tools)
  - CMake 3.15+

### Установка:
```
git clone https://github.com/5c0uT/maze-anomaly-detector.git
cd maze-anomaly-detector
setup.bat
```

### Проверка установки:
```
python scripts\check_imports.py
```
Ожидаемый результат:
```
✅ maze_core успешно импортирован
✅ physics_core успешно импортирован
```

---

## Основные компоненты
### MazeGenerator
Класс для генерации 3D-лабиринтов

**Инициализация**:
```
from maze.generator import MazeGenerator

generator = MazeGenerator(width=50, height=50, depth=50, cell_size=1.0)
```

**Методы**:
| Метод | Параметры | Возвращаемое значение | Описание |
|-------|-----------|-----------------------|----------|
| `generate` | - | `np.ndarray` | Генерация воксельной сетки лабиринта |
| `find_path` | `start: tuple`, `end: tuple` | `List[tuple]` | Поиск пути между точками |

### DefectAnalyzer
Класс для анализа 3D-моделей на дефекты

**Инициализация**:
```
from detector.analyzer import DefectAnalyzer

analyzer = DefectAnalyzer(tolerance=0.001)
```

**Методы**:
| Метод | Параметры | Возвращаемое значение | Описание |
|-------|-----------|-----------------------|----------|
| `analyze` | `model_path: str` | `dict` | Анализ модели на дефекты |
| `calculate_volume` | `mesh: Trimesh` | `float` | Расчет объема модели |

### PhysicsValidator
Класс для физической валидации путей

**Инициализация**:
```
from validator import PhysicsValidator

validator = PhysicsValidator(cell_size=1.0)
```

**Методы**:
| Метод | Параметры | Возвращаемое значение | Описание |
|-------|-----------|-----------------------|----------|
| `validate` | `grid: np.ndarray`, `start: tuple`, `end: tuple` | `bool` | Проверка проходимости пути |

---

## Работа с CLI
### Генерация лабиринта
```
python generate_maze.py --size 50x50x50 --cell 1.5 --output maze.gltf
```
**Параметры**:
- `--size`: Размеры лабиринта (ширина x высота x глубина)
- `--cell`: Размер ячейки в метрах
- `--output`: Путь для сохранения GLTF-файла

### Детекция дефектов
```
python detect_defects.py model.stl --tolerance 0.005 --visualize defects.jpg --report report.html
```
**Параметры**:
- `model`: Путь к 3D-модели (STL, OBJ, GLTF)
- `--tolerance`: Чувствительность детектора (0.001-0.1)
- `--visualize`: Файл для визуализации дефектов
- `--report`: HTML-отчет с результатами

---

## Примеры использования
### Генерация и валидация лабиринта
```
from maze.generator import MazeGenerator
from validator import PhysicsValidator

# Генерация лабиринта
generator = MazeGenerator(30, 30, 30, 1.0)
grid = generator.generate()

# Валидация пути
validator = PhysicsValidator(1.0)
is_valid = validator.validate(grid, start=(0,0,0), end=(29,29,29))
print(f"Путь {'валиден' if is_valid else 'невалиден'}")
```

### Анализ модели на дефекты
```
from detector.analyzer import DefectAnalyzer

# Анализ модели
analyzer = DefectAnalyzer(tolerance=0.005)
results = analyzer.analyze("model.stl")

# Визуализация результатов
print(f"Найдено дефектов: {len(results['intersections']}")
print(f"Объем модели: {analyzer.calculate_volume(results['mesh'])}")
```

---

## Форматы данных
### Воксельная сетка
```
# 3D массив boolean значений
# True - проход, False - стена
grid = np.ndarray((depth, height, width), dtype=bool)
```

### Результаты детекции дефектов
```
{
    "intersections": np.array([[x1, y1, z1], ...]),  # Точки самопересечений
    "mesh": Trimesh  # Объект 3D-модели
}
```
