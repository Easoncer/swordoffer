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
    // 第一步新建链表
    void cloneNodes(RandomListNode * head)
    {
        RandomListNode * p = head;
        while(p != NULL)
        {
            RandomListNode * pnode = new RandomListNode(0);
            pnode->label =  p->label;
            pnode->next = p->next;
            pnode->random = NULL;

            p->next = pnode;
            p = pnode-> next;
        }
    }
    // 第二步定义复杂链表的指向

    void ConnectRandomNode(RandomListNode * head)
    {
        RandomListNode *p = head;
        while (p != NULL)
        {
            RandomListNode *pclone = p->next;
            if (p->random != NULL)
                pclone->random = p->random -> next;
            p = pclone->next;
        }
    }

    // 第三步 复制链表

    RandomListNode * ReconnectNode( RandomListNode * head)
    {
        RandomListNode *pNode = head;
        RandomListNode *pCloneHead = NULL;
        RandomListNode *pCloneNode = NULL;

        if (pNode != NULL)
        {
            pCloneHead = pCloneNode = head->next;
            pNode->next = pCloneHead -> next;
            pNode = pNode->next;
        }

        while (pNode != NULL)
        {
            pCloneNode -> next = pNode->next;
            pCloneNode = pCloneNode->next;
            pNode->next = pCloneNode->next;
            pNode = pNode->next;
        }
        return pCloneHead;
    }


    RandomListNode* Clone(RandomListNode* pHead)
    {
        cloneNodes(pHead);
        ConnectRandomNode(pHead);
        return ReconnectNode(pHead);
    }
};

int main()
{

    return 0;
}