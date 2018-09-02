//
// Created by 李先生 on 2018/8/31.
//
#include <iostream>
#include <string>
#include <vector>
#include <map>
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
    ListNode* FindFirstCommonNode( ListNode* pHead1, ListNode* pHead2) {
        if (pHead1 == NULL || pHead2 == NULL)
            return NULL;
        ListNode *p1 = pHead1;
        ListNode *p2 = pHead2;

        int len1 = 0, len2 = 0;
        while(p1 != NULL )
        {
            p1 = p1->next;
            len1 ++;
        }
        while (p2 != NULL)
        {
            p2 = p2->next;
            len2 ++;
        }
        cout << len1 << " "<<len2<<endl;

        p1 = pHead1, p2 =pHead2;
        if (len1 < len2)
        {
            int step = len2 -len1;
            while(step != 0)
            {
                p2 = p2->next;
                step -- ;
            }
        }

        if (len1 > len2)
        {
            int step = len1 -len2;
            while(step != 0)
            {
                p1 = p1->next;
                step -- ;
            }
        }

        while ( p1 != NULL && p2 != NULL)
        {
            if (p1->val == p2->val)
                return p1;
            p1 = p1->next;
            p2 = p2->next;
        }
        return NULL;

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

    ListNode *m1 = new ListNode(2);
    ListNode *m2 = new ListNode(3);
    ListNode *m3 = new ListNode(4);

    m1->next = m2;
    m2->next = m3;

    ListNode *res = s.FindFirstCommonNode(n1, m1);
    cout << res->val <<endl;
    return 0;
}