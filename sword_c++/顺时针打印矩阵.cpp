//
// Created by 李先生 on 2018/8/28.
//
#include <iostream>
#include <string>
#include <vector>
#include <stack>
using  namespace std;

class Solution {
public:
    vector<int> printCircle(vector<vector<int> > matrix, int start)
    {
        vector<int> res;
        int endx = matrix[0].size() -start;
        int endy = matrix.size()- start;

        for (int i = start; i < endx; i++)
        {
            res.push_back(matrix[start][i]);
//            cout << matrix[start][i]<< " ";
        }

//        cout << endl;

        if (start < endy-1 )
        {
            for (int i = start + 1; i < endy; i++)
            {
                res.push_back(matrix[i][endx-1]);
//                cout << matrix[i][endx-1]<< " ";
            }
        }

        //判断如果下边不存在的情况
        if (start < endy - 1 && start < endx - 1)
        {
            //如果 下边 存在
            for (int i = endx-2; i >= start ;i--)
            {
                res.push_back(matrix[endy-1][i]);
//                cout << matrix[endy-1][i]<< " ";
            }
        }

        //判断如果左边不存在情况
        if (start < endx - 1 && start < endy - 2)
        {
            //如果 左边 存在
            for (int i = endy-2; i > start ;i--)
            {
                res.push_back(matrix[i][start]);
//                cout << matrix[i][start]<< " ";
            }
        }
        return res;
    }
    vector<int> printMatrix(vector<vector<int> > matrix) {
        vector< int > res;
        int row = matrix.size(), col = matrix[0].size();
        if (row == 0|| col == 0)
            return res;
        int start = 0;

        //核心部分 主要控制循环的结束条件
        while (row > start *2 && col > start *2)
        {
            vector<int>tem = printCircle(matrix, start);
            for (int i = 0 ; i< tem.size();i++) res.push_back(tem[i]);
            start ++;
        }
        return  res;
    }
};

int main()
{
//    int a[] = {1,2,3,4};
    vector<int> s1 = {1,2,3,4};
    vector<int> s2 = {5,6,7,8};
    vector<int> s3 = {9,10,11,12};
    vector<int> s4 = {13,14,15,16};
    vector<vector <int>> s = { s1, s2, s3,s4};

    Solution st;
    vector<int> res =  st.printMatrix(s);

    for (int i =0 ; i< res.size(); i++)
        cout << res[i];
    return  0;
}
