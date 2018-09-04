//
// Created by 李先生 on 2018/9/4.
//

#include <iostream>
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
    vector<vector<int> > Print(TreeNode* pRoot) {
        vector< vector<int>> res;
        if (pRoot == NULL)
            return res;

        queue<TreeNode *>  tqueue;

        tqueue.push(pRoot);

        while(!tqueue.empty())
        {
            vector<int> temp;
            int number = tqueue.size();
            while (number)
            {
                TreeNode * node = tqueue.front();
                tqueue.pop();
                temp.push_back(node->val) ;

                if (node->left)
                    tqueue.push(node->left);
                if(node->right)
                    tqueue.push(node->right);
                number --;
            }
            res.push_back(temp);
        }
        return res;
    }

};

int main()
{

}