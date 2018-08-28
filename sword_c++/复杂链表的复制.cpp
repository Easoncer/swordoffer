//
// Created by 李先生 on 2018/8/29.
//
#include <iostream>
#include <vector>
#include <stack>
#include <string>
using namespace std;

struct RandomListNode {
    int label;
    struct RandomListNode *next, *random;
    RandomListNode(int x) :
            label(x), next(NULL), random(NULL) {
    }
};

class Solution {
public:
    RandomListNode* Clone(RandomListNode* pHead)
    {

    }
};

int main()
{
    return 0;
}