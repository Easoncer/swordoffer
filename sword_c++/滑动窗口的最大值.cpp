//
// Created by 李先生 on 2018/9/4.
//

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> maxInWindows(const vector<int>& num, unsigned int size)
    {
        vector<int> res;
        vector<int> indexqueue;

        if (num.empty() || size <= 0 || num.size() < size)
            return res;

        for (int i = 0 ; i < size; i++)
        {
            if(indexqueue.empty() || num[indexqueue.back()] > num[i] )
            {
                indexqueue.push_back(i);
            }
            else
            {
                while(!indexqueue.empty() &&num[indexqueue.back()] <= num[i])
                    indexqueue.pop_back();
                indexqueue.push_back(i);
            }
        }


//        初始化队列生成

        for (int i = size; i < num.size(); i++)
        {
            res.push_back(num[indexqueue.front()]);
            if (i - indexqueue.front() == size)
                indexqueue.erase(indexqueue.begin());

            if(indexqueue.empty() || num[indexqueue.back()] > num[i] )
            {
                indexqueue.push_back(i);
            }
            else
            {
                while(!indexqueue.empty() &&num[indexqueue.back()] <= num[i])
                    indexqueue.pop_back();
                indexqueue.push_back(i);
            }
        }
        res.push_back(num[indexqueue.front()]);

        return res;

    }
};

int main()
{
    Solution s;
    vector<int> te = {2,3,4,2,6,2,5,1};
    int size = 3;
    vector <int> res = s.maxInWindows(te, size);
    for (int i = 0; i< res.size(); i++)
        cout<< res[i]<<endl;
    return 0;
}