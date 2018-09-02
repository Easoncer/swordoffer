//
// Created by 李先生 on 2018/8/30.
//

#include <iostream>
#include <string>
#include <stack>
#include <vector>
#include <queue>
#include <map>
using namespace std;

class Solution {
public:
    int MoreThanHalfNum_Solution(vector<int> numbers) {

        map<int, int> str;
        int count = 0,i=0 ;
        for ( ; i< numbers.size(); i++)
        {
            count = ++str[numbers[i]] ;
            if (count > numbers.size()/2 )
                return numbers[i];
        }
        return 0;

    }
};

int main()
{
    vector<int> temp = {1,2,3,4,2,2,2,2};
    Solution s;
    int te =  s.MoreThanHalfNum_Solution(temp);
    cout << te << endl;
    return 0;
}