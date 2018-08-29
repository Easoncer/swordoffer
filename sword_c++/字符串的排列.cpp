//
// Created by 李先生 on 2018/8/29.
//
#include <iostream>
#include <stack>
#include <string>
#include <vector>
#include <queue>
#include <set>
using namespace std;

class Solution {
public:
    vector<string> res;
    string s;
    void dfs(string str, int step,vector<int> mark)
    {
        if (step == str.size())
        {
            res.push_back(s);
            return;
        }
        for (int i = 0 ; i< str.size(); i++)
        {
            if (mark[i] == 0)
            {
                mark[i] = 1;
                s.push_back(str[i]);
                dfs(str, step+1, mark);
                s.pop_back();
                mark[i] = 0;
            }
        }
    }
    vector<string> Permutation(string str) {
        if (str.size()== 0)
            return res;
        vector<int> mark ( str.size(), 0);
        dfs(str, 0, mark);

        set<string> reset;
        for(int i = 0 ; i< res.size(); i++)
            reset.insert(res[i]);

        res.clear();
        set<string >::iterator i;
        for (i = reset.begin() ; i != reset.end(); i++)
            res.push_back(*i);
        return res;
    }
};

int main()
{
    Solution s;
    vector<string> res = s.Permutation("aa");

    for (int i = 0; i<res.size();i++)
        cout<< res[i] << endl;
    return 0;
}

