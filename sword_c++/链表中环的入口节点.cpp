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
    ListNode* EntryNodeOfLoop(ListNode* pHead)
    {
        if (pHead == NULL || pHead->next == NULL || pHead-> next ->next == NULL)
            return NULL;
        ListNode * slow = pHead->next;
        ListNode * fast = pHead -> next -> next;
        while (fast->next && fast -> next->next && slow != fast)
        {
            slow = slow->next;
            fast = fast->next->next;
        }
        if (fast->next == NULL || fast->next->next == NULL)
            return NULL;
        fast = pHead;

        while (fast != slow)
        {
            fast = fast->next;
            slow = slow->next;
        }
        return fast;
    }
};

int main()
{
    ListNode *n1 = new ListNode(1);
    ListNode *n2 = new ListNode(2);
    ListNode *n3 = new ListNode(3);
    ListNode *n4 = new ListNode(4);

    n1->next = n2;
    n2->next = n3;
    n3->next = n4;
    n4->next = n2;
    Solution s;
    ListNode *res = s.EntryNodeOfLoop(n1);

    cout <<res->val <<endl;
    return 0;
}