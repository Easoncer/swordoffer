//
// Created by 李先生 on 2018/8/28.
//

#include <iostream>
#include <stack>
#include <string>
#include <vector>
using namespace std;

class Solution {
private:
    stack<int> s;
    stack<int> mins;

public:

    void push(int value) {
        s.push(value);

        if (mins.empty() ||value <= mins.top())
        {
            mins.push(value);
        }
    }
    void pop() {
        if (s.empty())
        {
            return;
        }
        int num = s.top(), minnum = mins.top();
        if (num != minnum)
        {
            s.pop();
        }
        else
        {
            s.pop();
            mins.pop();
        }
    }
    int top() {
        return s.top();
    }
    int min() {
        return mins.top();
    }
};

int main()
{
    Solution s;
    s.push(3);
    s.push(3);
    s.push(4);
    s.push(5);
    cout << s.top()<<endl;
    return  0;

}