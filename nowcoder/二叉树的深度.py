# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 二叉树的深度.py

@time: 2018/5/28 上午10:40

'''
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot is None:
            return 0
        return max(self.TreeDepth(pRoot.left)+1, self.TreeDepth(pRoot.right)+1)

if __name__ == '__main__':
    pass

