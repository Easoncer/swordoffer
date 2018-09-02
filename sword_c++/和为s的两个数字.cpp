//
// Created by 李先生 on 2018/9/1.
//
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> FindNumbersWithSum(vector<int> array,int sum) {
        vector<int> res;
        if (array.size()<2)
            return res;
        int left = 0, right = array.size()-1;
        while (left < right)
        {
            if (array[left] + array[right] == sum)
            {
                res = {array[left] , array[right] };
                break;
            }
            if (array[left] + array[right] < sum)
            {
                left ++;
            }
            if (array[left] + array[right] > sum)
            {
                right --;
            }
        }
        return res;
    }
};

int main()
{
    vector<int> temp = {1,4,5,6,8,9};
    Solution s;
    vector <int> res = s.FindNumbersWithSum(temp, 9);
    for(int i = 0; i< res.size();i++)
        cout << res[i] <<endl;
    
    return 0;
}