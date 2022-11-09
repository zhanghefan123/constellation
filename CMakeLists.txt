cmake_minimum_required(VERSION 3.23)
project(c___learning)

set(CMAKE_CXX_STANDARD 14)

include_directories(./cpp_basic)

add_executable(c___learning
        cpp_basic/source/CinAndCout.cpp
        cpp_basic/source/ConcatStringWithSStream.cpp
        cpp_basic/source/InlineFunction.cpp
        cpp_basic/source/MacroTest.cpp
        cpp_basic/Main.cpp)