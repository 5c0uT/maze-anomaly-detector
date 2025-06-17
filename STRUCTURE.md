maze-anomaly-detector/
├── core/              - Исходники и сборка C++ модулей
│   ├── CMakeLists.txt - Конфигурация сборки
│   ├── defect_core.cpp - Детекция дефектов
│   ├── maze_core.cpp  - Генерация лабиринта
│   ├── physics_core.cpp - Физическая валидация
│   └── build/         - Директория сборки
├── detector/          - Модуль детекции дефектов
│   ├── analyzer.py    - Анализ 3D-моделей
│   ├── reporter.py    - Генерация отчетов
│   └── visualizer.py  - Визуализация дефектов
├── maze/              - Модуль генерации лабиринтов
│   ├── exporter.py    - Экспорт в GLTF
│   ├── generator.py   - Алгоритмы генерации
│   └── validator.py   - Физическая валидация
├── scripts/           - Вспомогательные скрипты
│   ├── build_core.bat - Сборка C++ модулей
│   └── check_imports.py - Проверка зависимостей
├── .venv/             - Виртуальное окружение
├── setup.bat          - Автоматизация установки
├── requirements.txt   - Python зависимости
├── generate_maze.py   - CLI генерации лабиринта
└── detect_defects.py  - CLI детекции дефектов