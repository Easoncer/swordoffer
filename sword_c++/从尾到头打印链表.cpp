//
// Created by 李先生 on 2018/8/26.
//

#include <iostream>
#include <vector>
#include <string>
#include<algorithm>
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
    vector<int> printListFromTailToHead(ListNode* head) {
        vector<int> linkNum;
        if (head == nullptr)
            return linkNum;
        while (head != nullptr)
        {
            linkNum.push_back(head -> val);
            head = head -> next;
        }
        reverse(linkNum.begin(), linkNum.end());
        return linkNum;
    }
};

int main(){
    ListNode a= {4}, b= {1}, c={3}, d = {7}, e = {0};
    a.next = &b, b.next = &c, c.next = &d, d.next = &e;

    Solution s;

    vector<int> linkNum = s.printListFromTailToHead(&a);
    for (int i = 0 ; i< linkNum.size(); i++)
        cout << linkNum[i] <<endl;

    return 0;
}
