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
//    int min (int a, int b, int c)
//    {
//        int minn ;
//        if (a < b && a < c)
//            minn = a;
//        if (b < a && b < c)
//            minn = b;
//        if (c < b && c < a)
//            minn =  c;
//        return minn;
//    }

    int GetUglyNumber_Solution(int index) {
        vector<int> nums;
        nums.push_back(1);
        if (index == 1) return nums[0];

        int k2 = 0, k3 = 0, k5 = 0 ;

        for (int i = 0; i < index-1 ; i++)
        {
            int minnum = min( nums[k2]*2, min(nums[k3]*3, nums[k5]*5));
            if (minnum == nums[k2]*2) k2++;
            if (minnum == nums[k3]*3) k3++;
            if (minnum == nums[k5]*5) k5++;
            nums.push_back(minnum);
        }
        return nums.back();
//        for (int i = 0 ; i< nums.size();i++)
//        {
//            cout << nums[i]<< endl;
//        }
    }
};

int main()
{
    Solution s;

    cout << s.GetUglyNumber_Solution(11);
    return 0;
}
