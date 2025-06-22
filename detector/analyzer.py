import sys
import os
import numpy as np
import trimesh

# Добавляем корень проекта в пути поиска
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import defect_core
except ImportError as e:
    print(f"Ошибка импорта defect_core: {e}")
    print("Пути поиска Python:")
    for path in sys.path:
        print(f" - {path}")

    print("\nСодержимое корня проекта:")
    try:
        print(os.listdir(project_root))
    except Exception as dir_err:
        print(f"Ошибка при чтении директории: {dir_err}")

    print("\nПроверка наличия defect_core.pyd:")
    core_files = [f for f in os.listdir(project_root) if f.startswith('defect_core')]
    print(f"Найдено файлов: {core_files}")

    raise


class DefectAnalyzer:
    def __init__(self, tolerance: float = 0.001):
        self.tolerance = tolerance
        self.core = defect_core.DefectCore()

    def analyze(self, model_path: str) -> dict:
        """Анализ 3D-модели на наличие дефектов"""
        # Загрузка модели
        mesh = trimesh.load(model_path, force='mesh')

        # Проверка водонепроницаемости
        if not mesh.is_watertight:
            mesh.fill_holes()

        # Подготовка данных для C++ ядра
        vertices = mesh.vertices.flatten().tolist()
        triangles = mesh.faces.flatten().tolist()

        # Поиск дефектов
        intersections = self.core.find_self_intersections(vertices, triangles)

        return {
            "intersections": np.array(intersections).reshape(-1, 3) if intersections else np.empty((0, 3)),
            "mesh": mesh
        }

    def calculate_volume(self, mesh: trimesh.Trimesh) -> float:
        """Расчет объема модели"""
        return mesh.volume
