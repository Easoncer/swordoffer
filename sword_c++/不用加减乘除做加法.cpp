//
// Created by 李先生 on 2018/9/2.
//
#include <iostream>
using namespace std;

class Solution {
public:
    int Add(int num1, int num2)
    {
        while (num2!=0) {
            int temp = num1^num2;
            num2 = (num1&num2)<<1;
            num1 = temp;
        }
        return num1;
    }
};

int main()
{
    Solution s;
    cout << s.Add(13, 14);
}
