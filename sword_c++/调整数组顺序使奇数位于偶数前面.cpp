//
// Created by 李先生 on 2018/8/27.
//
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    //快速排序不是一种稳定的算法
//    void reOrderArray(vector<int> &array) {
//        int i = 0, j = 0;
//        for (j = i; j < array.size(); j++ )
//        {
//            if (array[j] % 2 == 1)
//            {
//                int tem = array[i];
//                array[i] = array[j];
//                array[j] = tem;
//                i++;
//            }
//        }
//    }

    // 用一个数组存放  时间复杂度O(n) 空间复杂度O(n)
//    void reOrderArray(vector<int> &array) {
//        vector<int> res;
//        for (int i = 0; i < array.size(); i++)
//        {
//            if (array[i] % 2 == 0) res.push_back(array[i]);
//        }
//        for(int i = 0; i< array.size();i ++)
//        {
//            if (array[i] %2 == 1) res.push_back(array[i]);
//        }
//        array =res;
//    }

    //  采用插入排序的思想 时间复杂度O(n2)
    void reOrderArray(vector<int> &array) {
        for (int i = 0; i < array.size(); i++)
        {
            if (array[i] % 2 == 1) {
                int key = array[i];
                int index = i - 1;
                while ( index >= 0 && array[index] % 2 == 0) {
                    array[index+1] = array[index];
                    index --;
                }
                array[index+1] = key;
            }
        }
    }
};

int main()
{
    Solution s;
    vector<int >n = {1,2,3,4,5,6,7};
    s.reOrderArray(n);
    for (int i  = 0; i< n.size();i++)
        cout << n[i] <<endl;
    return 0;
}
