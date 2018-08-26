//
// Created by 李先生 on 2018/8/26.
//
#include <iostream>
#include <vector>
#include <string>
#include <stack>
using namespace std;

class Solution {
public:
    int minNumberInRotateArray(vector<int> rotateArray) {
        int left = 0, right = rotateArray.size() - 1, mid;
        while (left <= right)
        {
            mid = (left + right)/2;

            if (right - left == 1){
                return rotateArray[right];
            }

            if (rotateArray[left] == rotateArray[mid]  &&  rotateArray[mid] == rotateArray[right])
            {
                int min;
                for (int i = 1, min = 0; i < rotateArray.size(); i++) {
                    if (rotateArray[i] < rotateArray[min])
                        min = i;
                }
                return rotateArray[min];
            }
            if( rotateArray[left] > rotateArray[mid])
            {
                right = mid ;
            }
            if ( rotateArray[right] < rotateArray[mid])
            {
                left = mid ;
            }
        }
    }
};

int main()
{
    Solution s;
    vector<int> num = {1,1,0,1,1,1};
    int result = s.minNumberInRotateArray(num);
    cout << result << endl;
    return 0;
}

