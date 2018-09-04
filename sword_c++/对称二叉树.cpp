//
// Created by 李先生 on 2018/9/4.
//
#include <iostream>
#include <vector>
using namespace std;

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
    TreeNode(int x) :
            val(x), left(NULL), right(NULL) {
    }
};

class Solution {
public:
    bool isSymmetrical(TreeNode* pRoot)
    {
        if (pRoot == NULL)
            return true;
        return isSame(pRoot->left,pRoot->right);
    }

    bool isSame(TreeNode * root1, TreeNode *root2)
    {
        if (root1 == NULL && root2 == NULL)
            return true;
        if (root1 == NULL || root2 == NULL)
            return false;
        if (root1->val != root2->val)
            return false;
        else
            return isSame(root1->left, root2->right) && isSame(root1->right, root2->left);
    }
};

int main()
{
    return 0;
}
