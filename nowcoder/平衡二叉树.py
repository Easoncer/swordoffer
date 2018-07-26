# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 平衡二叉树.py

@time: 2018/5/28 上午10:44

'''


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        def TreeDepth(pRoot):
            if not pRoot:
                return 0
            return max(TreeDepth(pRoot.left), TreeDepth(pRoot.right)) + 1

        if not pRoot:
            return True
        if abs(TreeDepth(pRoot.left) - TreeDepth(pRoot.right)) <= 1:
            return True
        else:
            return False
        return (IsBalanced_Solution(pRoot.left)) and (IsBalanced_Solution(pRoot.right))

if __name__ == '__main__':
    pass

