//
// Created by 李先生 on 2018/9/4.
//
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool isRight(char* matrix, int rows, int cols, char* str, int row, int col,vector<int> &mark)
    {
        if(*str == '\0')
            return true;
        if(col> cols || col < 0 || row > rows || row < 0 )
            return false;
        int index = row*cols + col;
        bool res = false;

        if (mark[index]==0 && matrix[index] == str[0])
        {
            mark[index] = 1;
            res =  isRight(matrix, rows, cols, str+1,row+1, col, mark)
            || isRight(matrix, rows, cols, str+1,row-1, col, mark)
            || isRight(matrix, rows, cols, str+1,row, col+1, mark)
            || isRight(matrix, rows, cols, str+1,row, col-1, mark);
            mark[index] = 0;
        }

        return res;
    }

    bool hasPath(char* matrix, int rows, int cols, char* str)
    {

        vector<int> mark(strlen(matrix), 0);

        for(int i =0; i<rows; i++)
        {
            for(int j= 0; j<cols; j++)
            {
                if (isRight(matrix, rows, cols, str,i, j, mark ))
                {
                    return true;
                }
            }
        }
        return false;
    }
};

int main()
{
//    二维矩阵
    char matrix[] = "ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS";
    Solution s;
    char str[] = "SLHECCEIDEJFGGFIE";
    cout << s.hasPath(matrix, 5,8,str);

    return 0;
}
