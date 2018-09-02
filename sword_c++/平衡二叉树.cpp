//
// Created by 李先生 on 2018/8/31.
//
#include <iostream>
#include <string>
#include <vector>
#include <queue>
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
    bool  isBlance = true;

    int getDepth(TreeNode * root)
    {
        if (root  == NULL)
            return 0;

        int left = getDepth(root -> left);
        int right = getDepth( root -> right);

        if (abs(left - right) > 1 )
            isBlance = false;
        return right > left? right+1:left+1;

    }

    bool IsBalanced_Solution(TreeNode* pRoot) {
        getDepth(pRoot);
        return isBlance;
    }
};

int main()
{
    TreeNode * root = new TreeNode(10);
    TreeNode * left_1 = new TreeNode(6);
    TreeNode * right_1 = new TreeNode(14);
    root->left = left_1, root->right = right_1;

    TreeNode * left_2_1 = new TreeNode(4);
    TreeNode * right_2_1 = new TreeNode(5);
    left_1->left = left_2_1, left_1->right = right_2_1;

    TreeNode * left_2_2 = new TreeNode(12);
    TreeNode * right_2_2 = new TreeNode(16);
    right_1->left = left_2_2, right_1->right = right_2_2;

    Solution s;
    bool temp =  s.IsBalanced_Solution(root);
    cout << temp << endl;

    return 0;
}

