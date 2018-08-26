//
// Created by 李先生 on 2018/8/27.
//

#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int jumpFloorII(int number) {
        vector<int> s={1,1};
        if (number == 0 || number == 1){
            return s[number];
        }
        for (int i = 2; i< number +1 ;i++)
        {
            s.push_back(s[i-1]*2);
        }
        return s[number];
    }
};

int main()
{
    Solution s;
    cout << s.jumpFloorII(3) << endl;
    return 0;
}
