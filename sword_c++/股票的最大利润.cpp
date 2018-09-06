//
// Created by 李先生 on 2018/9/5.
//

#include <iostream>
#include <vector>
using namespace std;


int FindMost(vector<int> num)
{
    int res = 0;
    if (num.size()<0)
        return res;

    int min = num[0];
    for (int i = 1; i< num.size(); i++)
    {
        if(num[i]- min > res)
            res = num[i] - min;
        if (min > num[i])
            min = num[i];
    }
    return res;
}

int  main(){
    vector<int> s= {9,11,8,5,7,12,16,14};
    cout << FindMost(s)<<endl;
    return 0;
}