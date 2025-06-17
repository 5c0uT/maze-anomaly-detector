cmake_minimum_required(VERSION 3.15)
project(core)

# Настройки для Windows
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_MSVC_RUNTIME_LIBRARY "MultiThreaded$<$<CONFIG:Debug>:Debug>")

# Поиск pybind11
find_package(pybind11 REQUIRED)

# Создание модулей
pybind11_add_module(maze_core maze_core.cpp)
pybind11_add_module(physics_core physics_core.cpp)
pybind11_add_module(defect_core defect_core.cpp)

# Для Windows: установка выходного каталога
set_target_properties(maze_core physics_core defect_core PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY_RELEASE ${CMAKE_CURRENT_SOURCE_DIR}
    LIBRARY_OUTPUT_DIRECTORY_RELEASE ${CMAKE_CURRENT_SOURCE_DIR}
    ARCHIVE_OUTPUT_DIRECTORY_RELEASE ${CMAKE_CURRENT_SOURCE_DIR}
)