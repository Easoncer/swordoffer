//
// Created by 李先生 on 2018/8/27.
//
#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    int Fibonacci(int n) {
        vector<int> s = {0,1};
        if (n == 0 || n == 1)
        {
            return s[n];
        }
        for (int i = 2 ; i < n+1 ; i++ )
        {
            s.push_back(s[i-2] + s[i-1]);
        }
        return s[n];
    }
};

int main()
{
    Solution s;
    cout << s.Fibonacci(3) <<endl;
    return 0;
}
