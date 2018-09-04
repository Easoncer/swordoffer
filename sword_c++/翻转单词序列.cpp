//
// Created by 李先生 on 2018/9/2.
//

#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string ReverseSentence(string str) {
        string res = "";
        string temp = "";
        for(int i = 0; i< str.size(); i++)
        {
            if (str[i] == ' ')
            {
                temp = " " + temp;
                res = temp + res;
                temp = "";
                continue;
            }
            temp += str[i];
        }
        cout << temp <<endl;
        res = temp + res;
        return res;
    }
};

int main()
{
    string str = "I am a students.";
    Solution s;
    cout << s.ReverseSentence(str);
    return 0;
}

