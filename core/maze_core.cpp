#include <pybind11/pybind11.h>

namespace py = pybind11;

class MazeCore {
public:
    std::vector<bool> generate_prim(int width, int height, int depth) {
        // Простейшая реализация для теста
        int total = width * height * depth;
        std::vector<bool> grid(total, false);

        // Создаем простой проход по центру
        for (int y = 0; y < height; y++) {
            int idx = y * width * depth + (depth / 2) * width + (width / 2);
            if (idx < total) grid[idx] = true;
        }

        return grid;
    }
};

PYBIND11_MODULE(maze_core, m) {
    py::class_<MazeCore>(m, "MazeCore")
        .def(py::init<>())
        .def("generate_prim", &MazeCore::generate_prim);
}