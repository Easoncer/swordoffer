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
    int FindGreatestSumOfSubArray(vector<int> array) {
        int res = array[0], temp = array[0];
        for (int i = 1 ; i < array.size(); i++)
        {
            temp += array[i];
            if (temp > res)
                res = temp;

            if (temp < 0)
                temp = 0;
        }
        return res;

    }
};

int main()
{
    Solution s;
    vector<int> nums = {-3,-2,-1};
    cout << s.FindGreatestSumOfSubArray(nums);

}