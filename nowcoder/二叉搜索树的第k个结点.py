# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 二叉搜索树的第k个结点.py

@time: 2018/6/9 下午10:04

'''


class Solution:
    # 返回对应节点TreeNode

    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot or k == 0:
            return None

        res = self.sub_tree(pRoot)
        if k > len(res):
            return None
        else:
            return res[k - 1]

    def sub_tree(self, node):
        if not node:
            return None
        res = []
        if node.left:
            res.extend(self.sub_tree(node.left))
        res.append(node)

        if node.right:
            res.extend(self.sub_tree(node.right))
        return res

if __name__ == '__main__':
    pass

