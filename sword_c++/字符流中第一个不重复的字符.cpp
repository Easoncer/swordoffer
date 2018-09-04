//
// Created by 李先生 on 2018/9/4.
//
#include <iostream>
#include <map>
#include <string>
#include <queue>
using namespace std;

class Solution
{
public:
    queue<char> str_queue;
    map<char, int> str_count;

    void Insert(char ch)
    {
        map<char, int>::iterator iter;

        iter = str_count.find(ch);
        if ( str_count.empty()||iter == str_count.end())
        {
            str_count[ch] = 1;
            str_queue.push(ch);
        }
//        如果找到值
        if (iter != str_count.end())
        {
            str_count[ch] += 1;
            if (str_queue.front() == ch)
            {
                str_queue.pop();
                while ( !str_queue.empty() && str_count[str_queue.front()] != 1)
                    str_queue.pop();
            }
        }

    }
    char FirstAppearingOnce()
    {
        if (str_queue.empty())
            return '#';
        else
            return str_queue.front();
    }
};

int main()
{
    Solution s;
    s.Insert('g');
    cout << s.FirstAppearingOnce();
    s.Insert('o');
    cout << s.FirstAppearingOnce();
    s.Insert('o');
    cout << s.FirstAppearingOnce();
    s.Insert('g');
    cout << s.FirstAppearingOnce();
    s.Insert('l');
    cout << s.FirstAppearingOnce();
    s.Insert('e');
    cout << s.FirstAppearingOnce();
}
