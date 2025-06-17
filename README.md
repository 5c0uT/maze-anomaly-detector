# 3D Maze Generator and Anomaly Detector

Проект для генерации 3D-лабиринтов и детекции дефектов в 3D-моделях.

## Основные функции
- Генерация параметрических 3D-лабиринтов
- Физическая валидация проходимости
- Детекция самопересечений и дефектов в 3D-моделях
- Экспорт в формат GLTF
- Анаглифная визуализация дефектов
- HTML отчеты с результатами анализа

## Быстрый старт
```cmd
git clone https://github.com/5c0uT/maze-anomaly-detector.git
cd maze-anomaly-detector
setup.bat
python generate_maze.py --size 30x30x30 --output maze.gltf
python detect_defects.py maze.gltf --visualize defects.png --report report.html
