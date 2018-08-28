//
// Created by 李先生 on 2018/8/28.
//
#include <iostream>
#include <string>
#include <stack>
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
    vector<int> PrintFromTopToBottom(TreeNode* root) {
        queue<TreeNode *> nodeQueue;
        vector<int> res;
        if (root == NULL)
        {
            return res;
        }
        nodeQueue.push(root);
        while (!nodeQueue.empty())
        {
            TreeNode * p =  nodeQueue.front();
            res.push_back(p->val);
            nodeQueue.pop();

            if ( p->left )
            {
                nodeQueue.push(p->left);
            }
            if (p->right)
            {
                nodeQueue.push(p->right);
            }
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

    vector<int> res =  s.PrintFromTopToBottom(root);
    for (int i = 0 ; i< res.size();i++)
    {
        cout << res[i] <<endl;
    }
    return  0;
}