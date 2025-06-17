#!/usr/bin/env python3
import argparse
import sys
import os
import time

# Добавляем корень проекта в PYTHONPATH
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

try:
    from detector.analyzer import DefectAnalyzer
    from detector.visualizer import AnomalyVisualizer
    from detector.reporter import generate_html_report
except ImportError as e:
    print(f"Ошибка импорта: {e}")
    print("Текущий PYTHONPATH:", sys.path)
    raise


def main():
    parser = argparse.ArgumentParser(description='Detect defects in a 3D model.')
    parser.add_argument('model', type=str, help='Path to 3D model file')
    parser.add_argument('--tolerance', type=float, default=0.001, help='Detection tolerance')
    parser.add_argument('--visualize', type=str, help='Output visualization image')
    parser.add_argument('--report', type=str, help='Output HTML report path')

    args = parser.parse_args()

    print(f"Analyzing model: {args.model}")
    print(f"Tolerance: {args.tolerance}")
    start_time = time.time()

    analyzer = DefectAnalyzer(args.tolerance)
    results = analyzer.analyze(args.model)

    volume = analyzer.calculate_volume(results["mesh"])
    print(f"Model volume: {volume:.4f} cubic units")

    print(f"Detected {len(results['intersections'])} self-intersections")
    print(f"Analysis completed in {time.time() - start_time:.2f}s")

    if args.visualize:
        print(f"Generating visualization: {args.visualize}")
        visualizer = AnomalyVisualizer(results["mesh"])
        visualizer.anaglyph_render(results, args.visualize)

    if args.report:
        print(f"Generating report: {args.report}")
        generate_html_report(results, args.report)

    print("Done!")


if __name__ == "__main__":
    main()