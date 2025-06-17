@echo off
setlocal enabledelayedexpansion

echo [1/5] Проверка CMake...
where cmake >nul 2>&1
if %errorlevel% neq 0 (
    echo ОШИБКА: CMake не найден в PATH
    echo Установите CMake и добавьте в системный PATH
    exit /b 1
)

echo [2/5] Создание директории сборки...
if not exist build mkdir build
cd build

echo [3/5] Генерация проекта...
cmake -G "Visual Studio 17 2022" -A x64 -DCMAKE_BUILD_TYPE=Release ..
if %errorlevel% neq 0 (
    echo ОШИБКА: Не удалось сгенерировать проект
    exit /b 1
)

echo [4/5] Сборка проекта...
cmake --build . --config Release
if %errorlevel% neq 0 (
    echo ОШИБКА: Сборка не удалась
    exit /b 1
)

echo [5/5] Копирование файлов...
copy Release\maze_core.pyd ..\..\ >nul
copy Release\physics_core.pyd ..\..\ >nul
copy Release\defect_core.pyd ..\..\ >nul

cd ..
echo Сборка успешно завершена!