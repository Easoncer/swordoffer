//
// Created by 李先生 on 2018/9/4.
//
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    // Parameters:
    //        numbers:     an array of integers
    //        length:      the length of array numbers
    //        duplication: (Output) the duplicated number in the array number
    // Return value:       true if the input is valid, and there are some duplications in the array number
    //                     otherwise false
    bool duplicate(int numbers[], int length, int* duplication) {
        int index = 0;
        for (int i = 0 ; i< length; i++)
        {
            int shift = numbers[i] % length;

            if (numbers[shift] > length)
            {
                *duplication = shift;
                return true;
            }
            else
                numbers[shift] += length;
        }
        return false;

    }
};

int main()
{
    Solution s;
    int numbers[] = {2,3,1,0,2,5,3};
    int dup;
    s.duplicate(numbers, 7, &dup);
    cout << dup<<endl;
    return 0;
}