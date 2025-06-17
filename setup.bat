@echo off
setlocal

echo ====================================================
echo  3D Maze Generator and Anomaly Detector
echo  Developed by 5c0uT
echo  Version: 1.0.0 | License: MIT
echo ====================================================
echo  Project Description:
echo  - Generates parameterized 3D mazes with physics validation
echo  - Detects defects in 3D models (self-intersections)
echo  - Exports to GLTF format with HTML reports
echo  - Optimized C++ core with Python interface
echo ====================================================

echo Создание виртуального окружения...
if not exist .venv python -m venv .venv

echo Активация виртуального окружения...
call .venv\Scripts\activate

echo Установка зависимостей...
pip install -r requirements.txt

echo Сборка C++ модулей...
cd core
call .\build_core.bat
cd ..

echo Проверка наличия PYD файлов...
dir core\*.pyd

echo Копирование модулей в корень проекта...
copy core\maze_core.pyd . >nul
copy core\physics_core.pyd . >nul
copy core\defect_core.pyd . >nul
echo   [OK] C++ modules copied

echo Настройка PYTHONPATH...
set PYTHONPATH=%cd%;%PYTHONPATH%
echo   PYTHONPATH установлен в: %PYTHONPATH%

echo Проверка импорта модулей...
python scripts\check_imports.py

echo ====================================================
echo  Установка успешно завершена!
echo  Для генерации лабиринта выполните:
echo    python generate_maze.py --size 50x50x50 --output maze.gltf
echo
echo  Для проверки модели на дефекты:
echo    python detect_defects.py model.stl --visualize defects.png
echo ====================================================
echo  Проект: https://github.com/5c0uT/maze-anomaly-detector
echo  Автор: 5c0uT | 2023
echo ====================================================