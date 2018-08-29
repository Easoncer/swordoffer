//
// Created by 李先生 on 2018/8/29.
//
#include <iostream>
#include <string>
#include <vector>
#include <stack>
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
    //中序遍历
    //定义为全局变量
    TreeNode* head = NULL;
    TreeNode* Convert(TreeNode * pRootOfTree)
    {
        if (!pRootOfTree)
            return NULL;

        ConvertInorder(pRootOfTree);

        TreeNode* res = pRootOfTree;
        while(res ->left)
        {
            res = res ->left;
        }
        return res;
    }

    void ConvertInorder(TreeNode* pRootOfTree)
    {
        if (!pRootOfTree)
            return;
        ConvertInorder(pRootOfTree->left);

        pRootOfTree -> left = head;
        if (head) head->right = pRootOfTree;
        head = pRootOfTree;

        ConvertInorder(pRootOfTree->right);
    }
};

int main()
{
    Solution s;
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

    TreeNode * head = s.Convert(root);

    while(head ->right)
    {
        cout<< head->val << endl;
        head = head->right;
    }

    return 0;
}
