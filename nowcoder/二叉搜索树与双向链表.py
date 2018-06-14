# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 二叉搜索树与双向链表.py

@time: 2018/6/14 下午6:11

'''


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        self.arr = []
        self.midTraversal(pRootOfTree)

        for index, node in enumerate(self.arr[:-1]):
            node.right = self.arr[index + 1]
            self.arr[index + 1].left = node
        return self.arr[0]

    def midTraversal(self, root):
        if not root:
            return
        self.midTraversal(root.left)
        self.arr.append(root)
        self.midTraversal(root.right)

if __name__ == '__main__':
    pass

