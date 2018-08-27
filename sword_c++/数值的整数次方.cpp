//
// Created by 李先生 on 2018/8/27.
//
#include <iostream>
#include <vector>
#include <string>
#include <math.h>
using namespace std;

class Solution {
public:
    double unsignedPower(double base, int exponent) {
//        int res = 1;
        if (exponent == 0)
            return 1;
        if (exponent == 1)
            return base;

        double res = Power(base, exponent/2) ;
        res *= res;
        if (exponent % 2 == 1) res *= base;
        return res;
    }

    double Power(double base, int exponent){
        double result;
        if (base == 0) return 1;
        if (exponent < 0 ){
             result = unsignedPower(base, -1* exponent) ;
             result = 1.0/result;
        }
        else{
             result = unsignedPower(base,  exponent) ;
        }
        return result;
    }
};
int main()
{
    Solution s;
    cout << s.Power(2,-3);
    return 0;
}
