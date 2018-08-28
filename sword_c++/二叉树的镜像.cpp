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
    void Mirror(TreeNode *pRoot) {
        if (!pRoot)
        {
            return;
        }
        TreeNode * tem = pRoot->left;
        pRoot->left = pRoot->right;
        pRoot->right = tem;

        Mirror(pRoot->left);
        Mirror(pRoot->right);
    }
};

int main(){
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
    s.Mirror(root);
    cout << root->left->val << root->right->val<<endl;
    return 0;
}