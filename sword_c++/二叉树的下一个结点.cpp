//
// Created by 李先生 on 2018/9/4.
//
#include <iostream>
#include <vector>
using namespace std;

struct TreeLinkNode {
    int val;
    struct TreeLinkNode *left;
    struct TreeLinkNode *right;
    struct TreeLinkNode *next;
    TreeLinkNode(int x) :val(x), left(NULL), right(NULL), next(NULL) {}
};

class Solution {
public:
    TreeLinkNode* GetNext(TreeLinkNode* pNode)
    {
        if (pNode->right != NULL)
        {
            TreeLinkNode *temp = pNode->right;
            while (temp->left)
                temp = temp->left;
            return temp;
        }
        else
        {
            if (pNode-> next == NULL)
                return  NULL;
            while(pNode->next && pNode->next->left != pNode)
            {
                pNode = pNode->next;
            }
            return pNode->next;
        }
    }
};

int main()
{

    return 0;
}