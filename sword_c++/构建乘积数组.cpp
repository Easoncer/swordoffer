//
// Created by 李先生 on 2018/9/4.
//

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> multiply(const vector<int>& A) {
        vector<int> res;
        int temp = 1;
        res.push_back(temp);
        for(int i = 1 ;i < A.size(); i++)
        {
            temp *= A[i-1];
            res.push_back(temp);
        }
        temp = 1;
        for (int i= A.size()-1; i > 0; i--)
        {
            temp *= A[i];
            res[i-1] *= temp;
        }
        return res;
    }
};

int main()
{
    Solution s;
    vector<int> a = {1,2,3,4,5};
    vector <int> res = s.multiply(a);
    for(int i = 0; i<res.size(); i++)
        cout<<res[i]<<endl;
    return  0;
}