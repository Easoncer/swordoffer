//
// Created by 李先生 on 2018/8/26.
//

#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    void replaceSpace(char *str,int length) {
        if (str == nullptr || length == 0 )
            return;
        int originLen = 0, numBlank = 0;
        int i = 0;
        while (str[i] != '\0' )
        {
            originLen ++;
            if (str[i] ==' ')
                numBlank ++;
            i ++;
        }

        int newlen = originLen + numBlank*2;
        int indexOri= originLen, indexNew = newlen;

        while (indexOri >= 0 && newlen > indexOri)
        {
            if (str[indexOri] != ' ')
            {
                str[indexNew--] = str[indexOri--];
            }
            else {
                str[indexNew--] = '0';
                str[indexNew--] = '2';
                str[indexNew--] = '%';
                indexOri--;
            }
        }
//        for (int i=0 ; i< strlen(str); i++)
//            cout << str[i] << endl;
    }

};

int main()
{
    Solution s;
    char str[] = "as df";
    s.replaceSpace( str, '4');
    return 0;
}

