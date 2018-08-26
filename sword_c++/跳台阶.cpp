//
// Created by 李先生 on 2018/8/27.
//
#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    int jumpFloor(int number) {
        vector<int> s = {0,1,2};
        if (number == 1 || number == 2){
            return s[number];
        }
        for (int i = 3; i< number+1; i++)
        {
            s.push_back(s[i-2]+s[i-1]);
        }
        return s[number];
    }
};

int main()
{
    Solution s;
    cout << s.jumpFloor(4) << endl;
    return 0;
}
