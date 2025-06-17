import numpy as np
import defect_core
import trimesh


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