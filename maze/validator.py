import sys
import os
import importlib.util
import numpy as np


class PhysicsValidator:
    def __init__(self, cell_size: float):
        self.cell_size = cell_size
        self.core = self.load_core_module("physics_core", "PhysicsValidator")

    def load_core_module(self, module_name, class_name):
        """Динамическая загрузка C++ модуля"""
        # Пути для поиска модуля
        search_paths = [
            os.path.join(os.path.dirname(__file__), "..", "core", f"{module_name}.pyd"),
            os.path.join(os.path.dirname(__file__), f"{module_name}.pyd"),
            f"{module_name}.pyd"
        ]

        module_path = None
        for path in search_paths:
            if os.path.exists(path):
                module_path = path
                break

        if not module_path:
            # Формируем список путей для отображения в ошибке
            checked_paths = "\n".join([f" - {p}" for p in search_paths])
            raise ImportError(
                f"Не удалось найти модуль {module_name} по следующим путям:\n"
                f"{checked_paths}\n"
                "Убедитесь, что скрипт сборки core/build_core.bat был выполнен успешно."
            )

        print(f"Загрузка модуля {module_name} из {module_path}")

        # Динамическая загрузка модуля
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        return getattr(module, class_name)()

    def validate(self, grid: np.ndarray, start: tuple, end: tuple) -> bool:
        """Проверка проходимости лабиринта с физической моделью"""
        from .generator import MazeGenerator

        # Создаем временный генератор для поиска пути
        temp_maze = MazeGenerator(grid.shape[2], grid.shape[1], grid.shape[0], self.cell_size)
        temp_maze.grid = grid

        # Поиск пути
        path = temp_maze.find_path(start, end)
        if not path:
            print("Путь не найден!")
            return False

        # Конвертация пути в мировые координаты
        world_path = []
        for point in path:
            x, y, z = point
            world_path.append([
                x * self.cell_size,
                y * self.cell_size,
                z * self.cell_size
            ])

        # Параметры агента
        agent_radius = max(0.3 * self.cell_size, 0.5)
        step_height = 0.25 * self.cell_size

        # Физическая проверка
        return self.core.validate_path(world_path, agent_radius, step_height)


# Пример использования (для тестирования)
if __name__ == "__main__":
    print("Тестирование валидатора...")
    validator = PhysicsValidator(1.0)

    # Создаем простой лабиринт (прямой проход)
    grid = np.ones((5, 5, 5), dtype=bool)  # Все стены
    grid[:, :, 2] = False  # Вертикальный проход

    start = (2, 0, 2)
    end = (2, 4, 2)

    print("Результат валидации:", validator.validate(grid, start, end))