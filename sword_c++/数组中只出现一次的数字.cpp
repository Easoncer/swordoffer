//
// Created by 李先生 on 2018/9/1.
//
#include <iostream>
#include <iostream>
#include <string>
#include <stack>
#include <vector>
#include <queue>
#include <map>
using namespace std;

class Solution {
public:
    void FindNumsAppearOnce(vector<int> data,int* num1,int *num2) {
        int xordata = data[0];
        for (int i = 1; i< data.size(); i++)
            xordata = xordata xor data[i];
        unsigned int flag = 1;

        while (flag )
        {
            if (flag & xordata)
                break;
            flag = flag << 1;
        }
        vector<int> res1, res2;
        for (int i = 0 ;i< data.size(); i++)
        {
            if (data[i] & flag)
            {
                res1.push_back(data[i]);
            }
            else
            {
                res2.push_back(data[i]);
            }

        }

        *num1 = res1[0];
        *num2 = res2[0];
        for (int i = 1; i< res1.size();i++)
            *num1 = *num1 xor res1[i];

        for (int i = 1; i< res2.size();i++)
            *num2 = *num2 xor res2[i];
    }
};

int main()
{
    vector<int> list = { 1,3};
    int num1 = 0;
    int num2 = 0;
    Solution s;
    s.FindNumsAppearOnce(list, & num1, & num2);
    cout << num1 <<" "<< num2<<endl;
    return  0;
}
