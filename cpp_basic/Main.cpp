//
// Created by huang aoan on 2022/11/9.
//

# include <iostream>
# include "headers/ConcatStringWithSStream.h"
# include "headers/CinAndCout.h"
# include "headers/InlineFunction.h"

using namespace std;

int main()
{
    // 测试1：cin cout 测试
    cpp_basic::CinAndCoutTest();
    // 测试2：字符串连接测试
    string str1 = "hello";
    string str2 = "world";
    string split = " ";
    string result = cpp_basic::concatStringWithSStream(str1, str2, split);
    cout << result;
    // 测试3：内联函数测试
    int a = 3;
    int b = 4;
    int *a_pointer = &a;
    int *b_pointer = &b;
    cpp_basic::inlineSwap(a_pointer,b_pointer);
    cout << a << ',' << b << endl;
}