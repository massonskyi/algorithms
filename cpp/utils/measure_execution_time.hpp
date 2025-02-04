#ifndef __MEASURE_EXECUTION_TIME_HPP__
#define __MEASURE_EXECUTION_TIME_HPP__

#include <chrono>
#include <functional>
#include <iostream>
#include <type_traits>
namespace utils {

template <typename Func, typename... Args>
decltype(auto) 
measure_execution_time(Func&& func, Args&&... args) {
    auto start = std::chrono::steady_clock::now();

    if constexpr (std::is_invocable_v<Func, Args...>) {
        if constexpr (std::is_void_v<std::invoke_result_t<Func, Args...>>) {
            std::invoke(std::forward<Func>(func), std::forward<Args>(args)...);
            auto end = std::chrono::steady_clock::now();
            std::cout << "Execution time: "
                      << std::chrono::duration<double, std::milli>(end - start).count()
                      << " ms" << std::endl;
        } else {
            decltype(auto) result = std::invoke(std::forward<Func>(func), std::forward<Args>(args)...);
            auto end = std::chrono::steady_clock::now();
            std::cout << "Execution time: "
                      << std::chrono::duration<double, std::milli>(end - start).count()
                      << " ms" << std::endl;
            return result;
        };
    };
};
} // utils

#endif // __MEASURE_EXECUTION_TIME_HPP__