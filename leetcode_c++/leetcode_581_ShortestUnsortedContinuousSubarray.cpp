//
// Created by 李先生 on 2018/9/6.
//
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        int maxnum = nums[0];
        int end= 0;
        int minnum = nums[nums.size()-1];
        int start = nums.size()-1;

        for (int i = 1; i< nums.size();i++)
        {
            if (maxnum > nums[i])
                end = i;
            maxnum = max(nums[i], maxnum);
        }

        //  vector<int> temp = {2, 6, 4, 8, 10, 9, 15};
        for(int i = nums.size()-1; i >=0 ; i--)
        {
            if (minnum < nums[i])
                start = i;
            minnum = min(nums[i], minnum);
        }
//        cout  << start <<" " <<end<<endl;
        return  end - start + 1;
    }
};

int main()
{
    Solution s;
    vector<int> temp = {1,3,2,2,2};
    cout << s.findUnsortedSubarray(temp);
    return 0;
}
