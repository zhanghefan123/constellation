//
// Created by huang aoan on 2022/11/9.
//

#include <iostream>
#include <sstream>

using namespace std;

namespace cpp_basic{
    // 在这里我们可以进行字符串的拼接
    string concatStringWithSStream(string str1, string str2, string split) {
        /*
         * @param str1: 第一个字符串
         * @param str2: 第二个字符串
         * @param split: 两个字符串之间的分隔符
         * */
        stringstream ss;
        ss << str1 << split << str2 << endl;
        return ss.str();
    }
}
