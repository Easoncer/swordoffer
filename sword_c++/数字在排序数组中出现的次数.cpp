//
// Created by 李先生 on 2018/8/31.
//

#include <iostream>
#include <vector>
#include <string>
using  namespace std;

class Solution {
public:
    // 二分 分别判断数字的前和后的index
    // 从排序数组中找出第一个数字的索引

    int FindLeft(vector<int> data ,int k) {
        int left = 0, right = data.size()-1;
        while (left <= right)
        {
            int mid = (left+right)/2;

            if (data[mid] > k) right = mid - 1;
            if (data[mid] < k) left = mid + 1;

            if (data[mid] == k)
            {
                if (mid == 0 || data[mid -1] != k )
                    return mid;
                right = mid;
            }
        }
        return -1;
    }

    int FindRight(vector<int> data ,int k) {
        int left = 0, right = data.size()-1;
        while (left <= right)
        {
            int mid = (left+right + 1)/2;
            if (data[mid] > k) right = mid - 1;
            if (data[mid] < k) left = mid + 1;
//            cout << left << mid << right <<endl;
            if (data[mid] == k)
            {
                if (mid == data.size() - 1 || data[mid + 1] != k   )
                    return mid;
                left = mid;
            }
        }
        return -1;
    }

    int GetNumberOfK(vector<int> data ,int k) {
        int left = FindLeft(data, k);
        int right = FindRight(data, k);
        if (left == -1)
            return 0;
        return right - left + 1;
    }
};

int main()
{
    Solution s;
    vector<int> list = {1,3,4,4,4,4,6,7,10};

    cout << s.GetNumberOfK(list, 4) << endl;
    return 0;
}