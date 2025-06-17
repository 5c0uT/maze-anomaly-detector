import numpy as np
import random


class MazeGenerator:
    def __init__(self, width: int, height: int, depth: int, cell_size: float = 1.0):
        self.width = width
        self.height = height
        self.depth = depth
        self.cell_size = cell_size

    def generate(self) -> np.ndarray:
        """Генерация простого лабиринта для тестирования"""
        # Создаем все стены
        grid = np.zeros((self.depth, self.height, self.width), dtype=bool)

        # Создаем вертикальный проход по центру
        center_x = self.width // 2
        center_z = self.depth // 2

        for y in range(self.height):
            grid[center_z, y, center_x] = True

        # Создаем горизонтальный проход на верхнем уровне
        for x in range(self.width):
            grid[center_z, self.height - 1, x] = True

        return grid

    def find_path(self, start: tuple, end: tuple) -> list:
        """Упрощенный поиск пути"""
        return [start, (start[0], self.height - 1, start[2]), end]


# Тестирование генератора
if __name__ == "__main__":
    print("Тестирование генератора лабиринтов...")
    gen = MazeGenerator(10, 10, 10, 1.0)
    maze = gen.generate()
    print(f"Размер лабиринта: {maze.shape}")
    print(f"Количество проходов: {np.sum(maze)}")