#include "utils/measure_execution_time.hpp"
#include "pkg/shell_sort.hpp"
#include <vector>
#include <array>
#include <iostream>
#include <random>

template <typename T>
void fill_random_array(std::vector<T> &arr, long long size, int min, int max)
{
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(min, max);

    for (int i = 0; i < size; ++i)
    {
        arr.push_back(dis(gen));
    }
}
template <typename T, long long N>
void fill_random_array(std::array<T, N> &arr, int min,  int max)
{
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(min, max);

    for (int i = 0; i < N; ++i)
    {
        arr.push_back(dis(gen));
    }
}
template <typename T, long long N>
void fill_random_array(T (&arr)[N], int min, int max)
{
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(min, max);

    for (int i = 0; i < N; ++i)
    {
        *(arr + i) = (dis(gen));
    }
}
int main(int argc, char **argv)
{
    // std::array<int, 8> arr = {5, 2, 8, 1, 3, 6, 7, 4};
    std::vector<long long> arr;
    fill_random_array(arr, 1000, 1, 1000);
    std::cout << "Before sorting: ";

    for (int i : arr)
    {
        std::cout << i << " ";
    }
    std::cout << std::endl;

    utils::measure_execution_time([&arr]()
                                  { shell_sort(arr); });

    std::cout << "After sorting: ";
    for (int i : arr)
    {
        std::cout << i << " ";
    }
    std::cout << std::endl;
    return 0;
}