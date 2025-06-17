import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LightSource


class AnomalyVisualizer:
    def __init__(self, mesh):
        self.mesh = mesh

    def anaglyph_render(self, defects: dict, output_file: str, resolution: tuple = (800, 600)):
        """Анаглифная визуализация дефектов"""
        fig = plt.figure(figsize=(resolution[0] / 100, resolution[1] / 100), dpi=100)
        ax = fig.add_subplot(111, projection='3d')

        # Визуализация модели
        ax.plot_trisurf(
            self.mesh.vertices[:, 0],
            self.mesh.vertices[:, 1],
            self.mesh.vertices[:, 2],
            triangles=self.mesh.faces,
            alpha=0.7,
            color='cyan'
        )

        # Визуализация дефектов
        if defects.get("intersections") is not None and len(defects["intersections"]) > 0:
            points = defects["intersections"]
            ax.scatter(
                points[:, 0], points[:, 1], points[:, 2],
                s=50, c='red', marker='o', alpha=0.9, label='Self-intersections'
            )

        # Настройки визуализации
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.legend()

        # Анаглифный эффект
        self.apply_anaglyph_effect(ax)

        plt.savefig(output_file, bbox_inches='tight')
        plt.close()

    def apply_anaglyph_effect(self, ax):
        """Применение анаглифного эффекта к графику"""
        # Создание двух кадров для разных глаз
        from matplotlib.colors import rgb_to_hsv, hsv_to_rgb

        # Получение текущих цветов
        for collection in ax.collections:
            colors = collection.get_facecolor()

            # Преобразование цветов для левого глаза (красный канал)
            hsv = rgb_to_hsv(colors[:, :3])
            hsv[:, 0] = 0.0  # Оттенок для красного
            colors_left = hsv_to_rgb(hsv)

            # Преобразование для правого глаза (синий/зеленый)
            hsv[:, 0] = 0.6  # Оттенок для голубого
            colors_right = hsv_to_rgb(hsv)

            # Комбинирование цветов
            combined_colors = np.zeros_like(colors)
            combined_colors[:, 0] = colors_left[:, 0]  # Красный канал
            combined_colors[:, 1] = colors_right[:, 1]  # Зеленый канал
            combined_colors[:, 2] = colors_right[:, 2]  # Синий канал
            combined_colors[:, 3] = colors[:, 3]  # Альфа канал

            collection.set_facecolor(combined_colors)