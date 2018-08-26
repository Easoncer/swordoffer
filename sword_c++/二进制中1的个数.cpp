//
// Created by 李先生 on 2018/8/27.
//
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int  NumberOf1(int n) {
        unsigned int flag = 1,count = 0;
        while (flag > 0)
        {
            if (flag & n )
                count += 1;
//            cout << count <<endl;
            flag = flag << 1;
        }
        return count;
    }
};

int main()
{
    Solution s;
    cout << s.NumberOf1(4);
    return 0;
}
