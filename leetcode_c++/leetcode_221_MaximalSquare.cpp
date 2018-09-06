//
// Created by 李先生 on 2018/9/6.
//
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        if (matrix.empty() || matrix[0].empty())
            return 0;
        int maxnum = 0;

        int rows = matrix.size(), cols = matrix[0].size();
        vector<vector<int > >mark(rows, vector<int> (cols,0));

        for (int i =  0; i< rows;i++)
        {
            if (matrix[i][0] == '1') {
                mark[i][0] = 1;
                maxnum = max(mark[i][0], maxnum);
            }
        }

        for (int j = 0; j< cols; j++)
        {
            if (matrix[0][j] == '1')
            {
                mark[0][j] = 1;
                maxnum = max(mark[0][j], maxnum);
            }
        }

        for (int i = 1 ; i< rows; i++)
        {
            for (int j = 1 ; j<cols;j++)
            {
                if (matrix[i][j] == '1')
                {
                    mark[i][j] = min(mark[i-1][j], min(mark[i-1][j-1], mark[i][j-1]))+1;
                    maxnum = max(mark[i][j], maxnum);
                }

            }
        }
        return maxnum * maxnum;
    }
};

int main(){
    vector <vector<char>> num = {{'1','0','1','0','0'},{'1','0','1','1','1'},{'1','1','1','1','1'}, {'1','0','0','1','0'}};
    Solution s;
    cout << s.maximalSquare(num) <<endl;
    return 0;
}
