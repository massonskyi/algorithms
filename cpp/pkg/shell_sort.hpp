#ifndef __SHELL_SORT_HPP__
#define __SHELL_SORT_HPP__

#include <type_traits>
#include <vector>
#include <array>

// Специализация для std::vector
template <typename T>
void shell_sort(std::vector<T>& arr) {
    size_t n = arr.size();
    for (size_t gap = n / 2; gap > 0; gap /= 2) {
        for (size_t i = gap; i < n; i++) {
            T key = *(arr.begin() + i);
            size_t j = i;
            while (j >= gap && *(arr.begin() + j - gap) > key) {
                *(arr.begin() + j) = *(arr.begin() + j - gap);
                j -= gap;
            }
            *(arr.begin() + j) = key;
        }
    }
};

// Специализация для std::array<T, N>
template <typename T, size_t N>
void shell_sort(std::array<T, N>& arr) {
    size_t n = arr.size();
    for (size_t gap = n / 2; gap > 0; gap /= 2) {
        for (size_t i = gap; i < n; i++) {
            T key = *(arr.begin() + i);
            size_t j = i;
            while (j >= gap && *(arr.begin() + j - gap) > key) {
                *(arr.begin() + j) = *(arr.begin() + j - gap);
                j -= gap;
            }
            *(arr.begin() + j) = key;
        }
    }
};

// Специализация для обычного массива
template <typename T, size_t N>
void shell_sort(T (&arr)[N]) {
    for (size_t gap = N / 2; gap > 0; gap /= 2) {
        for (size_t i = gap; i < N; i++) {
            T key = *(arr + i);
            size_t j = i;
            while (j >= gap && *(arr + j - gap) > key) {
                *(arr + j) = *(arr + j - gap);
                j -= gap;
            }
            *(arr + j) = key;
        }
    }
};

#endif // __SHELL_SORT_HPP__

