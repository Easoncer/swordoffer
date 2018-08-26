//
// Created by 李先生 on 2018/8/26.
//

//Definition for binary tree

#include <iostream>
#include <vector>
#include <string>
#include<algorithm>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    // pre 先序遍历 vin 中序遍历
    TreeNode* reConstructBinaryTree(vector<int> pre,vector<int> vin) {
        if (vin.empty() || pre.empty())
            return NULL;
        TreeNode *root = new TreeNode(pre[0]);
        int i;
        for (i = 0; i < vin.size() && vin[i] != pre[0];i++);
        vector<int> pre_left, in_left, pre_right, in_right;

        for(int j = 0 ; j < vin.size(); j++)
        {
            if (j < i )
            {
                pre_left.push_back(pre[j+1]);
                in_left.push_back(vin[j]);
            }
            if (i < j)
            {
                pre_right.push_back(pre[j]);
                in_right.push_back(vin[j]);
            }
        }
        root -> left = reConstructBinaryTree(pre_left, in_left );
        root -> right = reConstructBinaryTree(pre_right, in_right);
        return root;
    }
};

int main()
{
    Solution s;
    vector<int> pre = { 1, 2, 4, 7, 3, 5, 6, 8 };
    vector<int> in = { 4, 7, 2, 1, 5, 3, 8, 6 };
    TreeNode* root= s.reConstructBinaryTree(pre, in);
    cout << root->left -> val <<endl;
    return 0;
}
