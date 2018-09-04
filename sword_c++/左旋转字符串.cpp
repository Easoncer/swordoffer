//
// Created by 李先生 on 2018/9/2.
//
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string LeftRotateString(string str, int n) {
        string res = "";
        string left = "";
        for (int i = 0; i < n; i++)
            res += str[i];
        for (int i = n ; i< str.size(); i++)
            left += str[i];
        return left + res;
    }
};

int main()
{
    string str = "abcXYZdef";
    Solution s;
    cout << s.LeftRotateString(str,3);
    return 0;
}

