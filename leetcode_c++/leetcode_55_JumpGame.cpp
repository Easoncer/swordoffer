//
// Created by 李先生 on 2018/9/6.
//

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool jumpBack(vector<int>& nums, int index)
    {
        if (index == 0)
            return true;

        for (int i = 0; i< index; i++)
        {
            if (nums[i] >= index - i)
                return  jumpBack(nums, i);
        }
        return false;
    }

    bool canJump(vector<int>& nums) {
        int index = nums.size()-1;
//        cout << jumpBack(nums, index)<<endl;
        return jumpBack(nums, index);
    }
};

int main()
{
    Solution s;
    vector<int> temp = {3,2,1,0,4};
    cout << s.canJump(temp) <<endl;
    return 0;
}