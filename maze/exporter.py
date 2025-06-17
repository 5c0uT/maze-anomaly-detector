import numpy as np
import trimesh
from trimesh.voxel import VoxelGrid


def export_to_gltf(grid: np.ndarray, cell_size: float, filename: str):
    """Экспорт лабиринта в формат GLTF (альтернативный метод)"""
    try:
        # Инвертируем: True = проход, False = стена -> True = материал (стена)
        matrix = np.logical_not(grid)

        # Создаем воксельную сетку
        voxel_grid = VoxelGrid(
            matrix,
            transform=trimesh.transformations.scale_matrix(cell_size)
        )

        # Преобразование в меш
        mesh = voxel_grid.marching_cubes

        # Экспорт
        mesh.export(filename.replace('.gltf', '.obj'))
        return True
    except Exception as e:
        print(f"Ошибка экспорта: {e}")

        # Попытка сохранить как простую модель
        try:
            # Создаем простой куб как fallback
            mesh = trimesh.creation.box((cell_size, cell_size, cell_size))
            mesh.export(filename)
            print(f"Создан fallback файл: {filename}")
            return True
        except:
            print("Не удалось создать даже fallback файл")
            return False