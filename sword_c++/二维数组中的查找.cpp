//
// Created by 李先生 on 2018/8/26.
//
#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    bool Find(int target, vector<vector<int> > array) {
        int col_index = array[0].size() - 1 , row_index = 0;

        while (col_index >= 0 && row_index < array.size()){
            if (array[row_index][col_index] == target)
                return true;
            else if ( array[row_index][col_index] > target)
                col_index --;
            else
                row_index ++;
        }
        return false;
    }
};

int main(){
    Solution s;
    vector< vector<int>>arr;
    for (int i = 0 ; i < 3; i++) {
        vector<int> temp;
        for (int j = 0; j < 3; j++)
            temp.push_back(j);
        arr.push_back(temp);
    }

    cout << arr[0].size() << endl;

    if (s.Find(2, arr) )
        cout << "True";
    else
        cout << "False";
}
