//
// Created by 李先生 on 2018/8/28.
//
#include <iostream>
#include <stack>
#include <string>
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    bool VerifySquenceOfBST(vector<int> sequence) {
        if (sequence.empty())
            return false;
        if (sequence.size()== 1)
            return true;

        int key = sequence.back();
        vector<int> left, right;
        int i;
        for (i = 0; i< sequence.size(); i++)
        {
            if (sequence[i] < key)
                left.push_back(sequence[i]);
            if (sequence[i] > key)
                break;
        }

        for(int j = i; j < sequence.size()-1; j++)
        {
            if (sequence[j] < key)
                return false;
            right.push_back(sequence[j]);
        }

        if (!left.empty() && !right.empty())
            return VerifySquenceOfBST(left)  && VerifySquenceOfBST(right);
        else if (!left.empty())
            return VerifySquenceOfBST(left);
        else
            return VerifySquenceOfBST(right);

    }

};

int main()
{
    Solution s1;
    vector<int> s = { 9, 11,10,8};
    if (s1.VerifySquenceOfBST(s))
        cout<< "t" <<endl;
    else{
        cout <<"f"<<endl;
    }
    return 0;
}
