//
// Created by 李先生 on 2018/9/4.
//
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    bool match(char* str, char* pattern)
    {
        if (*str != '\0' && *pattern == '\0' )
            return false;
        if (*str == '\0' && *pattern == '\0' )
            return true;

        if ( *(pattern+1) != '*')
        {
            if (*str == *pattern || (*str != '\0' && *pattern == '.'))
                return match(str+1, pattern+1);
            else
                return false;
        }
        else
        {
                if (*str == *pattern || (*str != '\0' && *pattern == '.'))
                    return match(str, pattern+2) || match(str+1, pattern);
                else
                    return match(str, pattern+2);
        }
    }
};

int main()
{
    char str[] = {'a','a','a','\0'};
    char pattern[] = {'a','.','a','\0'};
//    cout << strlen(str)<<endl;
    Solution s;
    cout << s.match(str, pattern);

    return 0;
}
