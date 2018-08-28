//
// Created by 李先生 on 2018/8/28.
//

#include <iostream>
#include <string>
#include <vector>
#include <stack>
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
    vector<vector <int>> res;
    vector<int> temp;
    vector<vector<int> > FindPath(TreeNode* root,int expectNumber) {

        if (root == NULL)
        {
            return res;
        }
        if (expectNumber == root->val && root->left == NULL && root->right == NULL)
        {
            temp.push_back(root->val);
            res.push_back(temp);
            temp.pop_back();
            return res;
        }
        if (root -> left != NULL)
        {
            temp.push_back(root->val);
            FindPath(root->left, expectNumber - root->val);
            temp.pop_back();
        }
        if (root -> right != NULL)
        {
            temp.push_back(root->val);
            FindPath(root-> right, expectNumber - root->val);
            temp.pop_back();
        }
        return res;
    }
};

int main()
{
    TreeNode * root = new TreeNode(1);
    TreeNode * left_1 = new TreeNode(2);
    TreeNode * right_1 = new TreeNode(3);
    root->left = left_1, root->right = right_1;

    TreeNode * left_2_1 = new TreeNode(4);
    TreeNode * right_2_1 = new TreeNode(5);
    left_1->left = left_2_1, left_1->right = right_2_1;

    TreeNode * left_2_2 = new TreeNode(3);
    TreeNode * right_2_2 = new TreeNode(7);
    right_1->left = left_2_2, right_1->right = right_2_2;

    Solution s;
    vector<vector <int>> res = s.FindPath(root, 7);
    for (int i =0 ; i< res[1].size();i++)
        cout << res[1][i]<<endl;
    return 0;
}