//
// Created by 李先生 on 2018/9/6.
//

#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
  };

class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        if ( head == NULL || head->next == NULL || head->next->next == NULL )
            return NULL;
        ListNode * slow = head->next, *fast = head->next->next;

        while (fast->next || fast->next->next)
        {
            fast = fast->next->next;
            slow = slow->next;
        }

        if (fast->next || fast->next->next)
            return NULL;

        fast = head;
        while (fast == slow)
        {
            fast = fast->next;
            slow = slow->next;
        }
        return  fast;
    }
};

int main()
{

    return 0;
}