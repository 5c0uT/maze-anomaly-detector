#include <vector>
#include <cmath>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

class PhysicsValidator {
public:
    bool validate_path(const std::vector<std::vector<float>>& path,
                      float agent_radius, float step_height) {
        // Упрощенная физическая проверка пути
        if (path.empty()) return false;

        // Проверка, что все точки достижимы
        for (size_t i = 1; i < path.size(); i++) {
            const auto& prev = path[i-1];
            const auto& curr = path[i];

            // Проверка высоты
            float height_diff = std::abs(curr[1] - prev[1]);
            if (height_diff > step_height) {
                return false;
            }

            // Проверка ширины прохода
            float dist = distance(prev, curr);
            if (dist < agent_radius * 1.5) {
                return false;
            }
        }
        return true;
    }

private:
    float distance(const std::vector<float>& p1, const std::vector<float>& p2) {
        float dx = p1[0] - p2[0];
        float dy = p1[1] - p2[1];
        float dz = p1[2] - p2[2];
        return std::sqrt(dx*dx + dy*dy + dz*dz);
    }
};

PYBIND11_MODULE(physics_core, m) {
    py::class_<PhysicsValidator>(m, "PhysicsValidator")
        .def(py::init<>())
        .def("validate_path", &PhysicsValidator::validate_path);
}