cmake_minimum_required(VERSION 3.10)
project(Algorithms)
set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Add the executable
add_executable(Algorithms 
    main.cxx
    pkg/shell_sort.hpp
    utils/measure_execution_time.hpp
    )
