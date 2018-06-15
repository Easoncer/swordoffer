# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 二叉树中和为某一值的路径.py

@time: 2018/6/14 下午10:03

'''


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def __init__(self):
        self.res = []
        self.temp = []

    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return self.res

        if expectNumber == root.val and not root.left and not root.right:
            self.temp.append(root.val)
            self.res.append(self.temp[:])
            self.temp.pop()

        if root.left:
            self.temp.append(root.val)
            self.FindPath(root.left, expectNumber - root.val)
            self.temp.pop()

        if root.right:
            self.temp.append(root.val)
            self.FindPath(root.right, expectNumber - root.val)
            self.temp.pop()

        return self.res

if __name__ == '__main__':
    pass

