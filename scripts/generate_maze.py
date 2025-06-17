#!/usr/bin/env python3
import argparse
import sys
import os
import time

print("="*50)
print("Начало выполнения скрипта generate_maze.py")
print("Текущая рабочая директория:", os.getcwd())
print("PYTHONPATH:", sys.path)

# Добавляем корень проекта в PYTHONPATH
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
    print(f"Добавлен в PYTHONPATH: {project_root}")

print("Обновленный PYTHONPATH:")
for p in sys.path:
    print(f" - {p}")
print("="*50)

# Добавляем корень проекта в PYTHONPATH
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

try:
    from maze.generator import MazeGenerator
    from maze.exporter import export_to_gltf
except ImportError as e:
    print(f"Ошибка импорта: {e}")
    print("Текущий PYTHONPATH:", sys.path)
    raise


def main():
    parser = argparse.ArgumentParser(description='Generate a 3D maze.')
    parser.add_argument('--size', type=str, default='50x50x50', help='Maze dimensions (width x height x depth)')
    parser.add_argument('--cell', type=float, default=1.0, help='Cell size in meters')
    parser.add_argument('--output', type=str, default='maze.gltf', help='Output GLTF file')

    args = parser.parse_args()
    dimensions = [int(d) for d in args.size.split('x')]

    if len(dimensions) != 3:
        raise ValueError("Size must be in format WxHxD")

    print(f"Generating {args.size} maze with cell size {args.cell}m...")
    start_time = time.time()

    generator = MazeGenerator(*dimensions, args.cell)
    grid = generator.generate()

    print(f"Generation completed in {time.time() - start_time:.2f}s")
    print(f"Exporting to {args.output}...")

    export_to_gltf(grid, args.cell, args.output)

    print("Done!")


if __name__ == "__main__":
    main()