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
    vector<TreeNode *> nodevec;

    void inorder(TreeNode * pRoot)
    {
        if (pRoot == NULL)
            return;
        inorder(pRoot->left);
        nodevec.push_back(pRoot);
        inorder(pRoot->right);
    }
    TreeNode* KthNode(TreeNode* pRoot, int k)
    {
        if (k <= 0 )
            return NULL;
        inorder(pRoot);
        if (nodevec.size() > k)
            return NULL;
        return nodevec[k-1];
    }
};

int main()
{
    vector<int> res;
    cout <<res.size()<<endl;
    return 0;
}


