//
// Created by 李先生 on 2018/8/27.
//
#include <iostream>
#include <vector>
#include <stack>
#include <string>
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
    ListNode* Merge(ListNode* pHead1, ListNode* pHead2)
    {
        if (pHead1 == NULL ){
            return pHead2;
        }
        if (pHead2 == NULL){
            return pHead1;
        }

        ListNode *head = new ListNode(0);
        if (pHead1->val < pHead2->val)
        {
            head->val = pHead1->val;
            head->next = Merge(pHead1 ->next, pHead2);
        }
        else
        {
            head->val = pHead2->val;
            head->next = Merge(pHead1, pHead2->next);
        }
        return head;
    }
};

int main()
{
    Solution s;
    ListNode * node1 = new ListNode(1);
    ListNode * node2 = new ListNode(3);
    ListNode * node3 = new ListNode(5);

    node1->next = node2;
    node2->next = node3;

    ListNode * node4 = new ListNode(2);
    ListNode * node5 = new ListNode(4);
    ListNode * node6 = new ListNode(6);

    node4->next = node5;
    node5->next = node6;

    ListNode *head = s.Merge(node1, node4);

    while (head != NULL){
        cout <<head->val<<endl;
        head = head->next;
    }

    return 0;
}
