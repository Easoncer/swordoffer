//
// Created by 李先生 on 2018/8/30.
//
#include <iostream>
#include <vector>
#include <stack>
#include <string>
#include <queue>
#include <map>

using namespace std;

class Solution {
public:
    int partition(vector<int> & input, int left, int right)
    {
        int key = input[right];
        int i = left, j= left;
        for (;j<right;j++)
        {
            if (input[j] < key)
            {
                int temp = input[i];
                input[i] = input[j];
                input[j] = temp;
                i++;
            }
        }
        int temp = input[i];
        input[i] = input[j];
        input[j] = temp;
        return i;
    }

    void GetLeastNumbers(vector<int> &input, int left, int right, int k) {

        int index = partition(input, left, right);
//        vector<int> res;

        if (index - left > k )
            GetLeastNumbers(input, left, index-1, k);
        if (index - left < k)
            GetLeastNumbers(input, index, right, k-index);
//        return res;
    }
    vector<int> GetLeastNumbers_Solution(vector<int> input, int k) {
        int left = 0, right = input.size()-1;
//        cout << left <<" "<< right <<" "<<k<<endl;
        GetLeastNumbers(input, left, right, k);
        vector <int > res;
        for (int i = 0; i< k;i++)
        {
            res.push_back(input[i]);
        }
        return res;
    }

};

int main ()
{
    Solution s;
    vector<int> temp = {1,4,3,2,7,6,5,9};
    vector <int> res = s.GetLeastNumbers_Solution(temp, 5);
    for (int i = 0; i< res.size(); i++)
        cout << res[i]<< endl;
    return 0;
}
