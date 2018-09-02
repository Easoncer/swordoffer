//
// Created by 李先生 on 2018/8/30.
//
#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;

class Solution {
public:
    int FirstNotRepeatingChar(string str)
    {
        map<char, int> dic;
        int i = 0;
        for (int i= 0; i< str.size(); i++)
        {
            dic[str[i]] ++;
        }
        for (i =0; i< str.size(); i++)
        {
            if (dic[str[i]] == 1)
            {
                return  i;
            }
        }

        return -1;

    }
};

int main()
{
    Solution s;
    string str= "asfas";
    cout << s.FirstNotRepeatingChar(str);
    return 0;
}
