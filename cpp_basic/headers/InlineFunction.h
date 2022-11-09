//
// Created by huang aoan on 2022/11/9.
//

#ifndef C___LEARNING_INLINEFUNCTION_H
#define C___LEARNING_INLINEFUNCTION_H
namespace cpp_basic{
    inline void inlineSwap(int* a, int*b)
    {
        int temp = *a;
        *a = *b;
        *b = temp;
    }
}
#endif //C___LEARNING_INLINEFUNCTION_H
