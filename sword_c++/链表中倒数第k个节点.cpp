//
// Created by 李先生 on 2018/8/27.
//
#include <iostream>
#include <vector>
#include <string>
using  namespace std;

struct ListNode {
	int val;
	struct ListNode *next;
	ListNode(int x) :
			val(x), next(NULL) {
	}
};

class Solution {
public:
    ListNode* FindKthToTail(ListNode* pListHead, unsigned int k) {
        if (pListHead == NULL){
            return NULL;
        }

        ListNode *p = pListHead;
        int step = 0;
        while (step != k   && p != NULL){
            p = p->next;
            step ++ ;
        }
        if (step <k){
            return NULL;
        }
        while (p != NULL)
        {
            pListHead = pListHead->next;
            p = p->next;
        }
        return pListHead;
    }
};

int main()
{
    Solution s;
    ListNode *n1 = new ListNode(1);
    ListNode *n2 = new ListNode(2);
    ListNode *n3 = new ListNode(3);

    ListNode *n4 = new ListNode(4);

    n1->next = n2;
    n2->next = n3;
    n3->next = n4;

    ListNode * p =  s.FindKthToTail(n1, 2);
    cout << p->val <<endl;
    return 0;
}