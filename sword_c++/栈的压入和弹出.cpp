//
// Created by 李先生 on 2018/8/28.
//

#include <iostream>
#include <stack>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    bool IsPopOrder(vector<int> pushV,vector<int> popV) {
        vector<int> temp;
        for (int i =0, j = 0 ; i< pushV.size(); i++)
        {
            temp.push_back(pushV[i]);

            while (j < popV.size() && temp[temp.size()-1] == popV[j])
            {
                temp.pop_back();
                j++;
            }
        }
        return temp.empty();
    }
};

int main()
{
    Solution s;
    vector<int> pushv = {1,2,3,4,5};
    vector<int> popv = {4,5,3,2,1};
    bool temp= s.IsPopOrder(pushv, popv);
    if (temp)
        cout<<"right";
    else
        cout <<"false";
    return 0;
}

