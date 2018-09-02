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
//    双指针问题
    vector<vector<int> > FindContinuousSequence(int sum) {

        int left = 1 ,right = 1, temp = 1;
        vector <vector<int>> res;
        if (sum == 1)
            return res;

        while (right <= (sum/2 + 1))
        {
            if (temp == sum)
            {
                vector<int> temp_res;
                for(int i = left; i < right+1; i++)
                    temp_res.push_back(i);
                res.push_back(temp_res);
                temp -= left;
                left ++;
            }
            if (temp > sum)
            {
                temp -= left;
                left ++;
            }
            if (temp < sum)
            {
                right ++;
                temp += right;
            }
        }
        return res;
    }
};

int main()
{
    Solution s;
    vector<vector<int> > res = s.FindContinuousSequence(3);
//    cout << res.size()<<endl;
    for(int i = 0 ;i < res.size(); i++)
        for (int j =0 ; j< res[i].size(); j++)
            cout << res[i][j]<<endl;
        cout << "----"<< endl;
    return  0;
}
