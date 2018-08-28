//
// Created by 李先生 on 2018/8/27.
//
#include <iostream>
#include <string>
#include <vector>
using  namespace std;

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
    bool isSame(TreeNode * p1, TreeNode *p2)
    {
        if (p2 == NULL)
            return true;
        if (p1 == NULL )
            return false;
        if (p1->val == p2->val)
            return isSame(p1->left, p2->left) && isSame(p1->right, p2->right);
        else
            return false;
    }
    bool HasSubtree(TreeNode* pRoot1, TreeNode* pRoot2)
    {
        if (pRoot1 == NULL || pRoot2 == NULL)
        {
            return false;
        }

        if (isSame(pRoot1, pRoot2))
            return true;
        bool res = false;
        if (pRoot1->left != NULL && !res)
        {
            res = HasSubtree( pRoot1->left, pRoot2);
        }
        if (pRoot1->right != NULL && !res)
        {
            res = HasSubtree( pRoot1->right, pRoot2);
        }
        return res;
    }
};

int main()
{
    Solution s;
    TreeNode * root = new TreeNode(1);
    TreeNode * left_1 = new TreeNode(2);
    TreeNode * right_1 = new TreeNode(3);
    root->left = left_1, root->right = right_1;

    TreeNode * left_2_1 = new TreeNode(4);
    TreeNode * right_2_1 = new TreeNode(5);
    left_1->left = left_2_1, left_1->right = right_2_1;

    TreeNode * left_2_2 = new TreeNode(6);
    TreeNode * right_2_2 = new TreeNode(7);
    right_1->left = left_2_2, right_1->right = right_2_2;

    TreeNode * root2 = new TreeNode(2);
    TreeNode * left2_1 = new TreeNode(4);
    TreeNode * right2_1 = new TreeNode(5);
    root2->left = left2_1, root2->right = right2_1;

    if (s.HasSubtree(root, root2))
    {
        cout << "right"<<endl;
    } else{
        cout <<"false"<<endl;
    }
    return  0;
}