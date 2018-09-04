//
// Created by 李先生 on 2018/9/4.
//
#include <iostream>
#include <vector>
using namespace std;

struct ListNode {
    int val;
    struct ListNode *next;
    ListNode(int x) :
        val(x), next(NULL) {
    }
};

class Solution {
public:
    ListNode* deleteDuplication(ListNode* pHead)
    {
        if (pHead == NULL)
            return NULL;
        ListNode *head = new ListNode(0);
        head->next = pHead;

        ListNode *p = head, *q =head->next;

        while(q && q->next)
        {
            if( q->val == q->next->val)
            {
                while (q->next && q->val == q->next->val)
                {
                    q = q->next;
                }
                p->next = q->next;
                q = q->next;
            }
            else
            {
                q = q->next;
                p = p->next;
            }
        }
        return head->next;

    }
};

int main()
{
    Solution s;
    ListNode *n1 = new ListNode(1);
    ListNode *n2 = new ListNode(2);
    ListNode *n3 = new ListNode(2);
    ListNode *n4 = new ListNode(3);
    ListNode *n5 = new ListNode(3);
    ListNode *n6 = new ListNode(4);
    n1->next = n2;
    n2->next = n3;
    n3->next = n4;
    n4->next = n5;
    n5->next = n6;

    ListNode *res = s.deleteDuplication(n1);
    cout <<res->val<<endl;
    return 0;
}