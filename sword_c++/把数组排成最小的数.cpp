//
// Created by 李先生 on 2018/8/30.
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
    static bool cmp (int i,int j)
    {
        string a = "";
        string b = "";
        a += to_string(i);
        a += to_string(j);
        b += to_string(j);
        b += to_string(i);

        return a<b;
    }

    string PrintMinNumber(vector<int> numbers) {
        string res = "";
        sort(numbers.begin(), numbers.end(), cmp);
        for(int i = 0; i < numbers.size(); i++)
            res += to_string(numbers[i]);
        return res;
    }
};

int main()
{
    Solution s;
    vector<int> sa = {3,32,321};
    cout << s.PrintMinNumber(sa);
    return 0;
}