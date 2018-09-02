//
// Created by 李先生 on 2018/8/31.
//

#include <iostream>
#include <string>
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
    int TreeDepth(TreeNode* pRoot)
    {
        if (pRoot == NULL)
        {
            return 0;
        }
        return max(TreeDepth(pRoot -> left) , TreeDepth( pRoot-> right)) + 1;
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

    cout << s.TreeDepth(root) << endl;
    return  0;
}