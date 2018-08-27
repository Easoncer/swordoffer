//
// Created by 李先生 on 2018/8/27.
//

#include <iostream>
#include <string>
#include <vector>
#include <stack>
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
    ListNode* ReverseList(ListNode* pHead) {
        if (pHead == NULL){
            return NULL;
        }
        stack<ListNode *> nodeStack;
        while (pHead != NULL)
        {
            nodeStack.push(pHead);
            pHead = pHead->next;
        }
        ListNode *head = new ListNode(0);
        ListNode *index = head;

        while (!nodeStack.empty() )
        {
            ListNode * p = nodeStack.top() ;
            nodeStack.pop();
            index->next = p;
            p->next = NULL;
            index = index->next;
        }
        return head->next;
    }
};

int main()
{
    Solution s;
    ListNode * node1 = new ListNode(1);
    ListNode * node2 = new ListNode(2);
    ListNode * node3 = new ListNode(3);

    node1->next = node2;
    node2->next = node3;

    ListNode *head=  s.ReverseList(node1);
    while (head != NULL){
        cout <<head->val<<endl;
        head = head->next;
    }
    return 0;
}