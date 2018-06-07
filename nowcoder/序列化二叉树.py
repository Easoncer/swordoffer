# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 序列化二叉树.py

@time: 2018/5/31 上午11:18

'''


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
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

