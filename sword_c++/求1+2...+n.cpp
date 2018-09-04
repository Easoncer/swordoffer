//
// Created by 李先生 on 2018/9/2.
//
#include <iostream>
using namespace std;

class Solution {
public:
    int Sum_Solution(int n) {
        int res = n;
        res && (res += Sum_Solution(n-1));
        return res;
    }
};
