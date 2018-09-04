//
// Created by 李先生 on 2018/9/2.
//

#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int LastRemaining_Solution(int n, int m)
    {
        if (m == 0 || n== 0)
            return -1;
        vector<int> list;
        for (int i = 0 ; i< n; i++)
            list.push_back(i);

        int num = n, start = 0;
        int index = 0;
        while (list.size() != 1)
        {
            index = (start + m - 1) % num ;
//            cout << list[index];
            list.erase(list.begin()+index);
            start = index;
            num --;
        }
        return list.front();
    }
};

int main()
{
    Solution s;
    cout << s.LastRemaining_Solution(3,1) ;
    return 0;
}