# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 6.py

@time: 2018/7/12 下午4:36

'''
class treeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def rebuild(preorder, inorder):
    if len(preorder) == 0:
        return  None

    root = treeNode(preorder[0])

    root.left = rebuild(preorder[1:inorder.index(preorder[0])+1], inorder[:inorder.index(preorder[0])])
    root.right = rebuild(preorder[inorder.index(preorder[0])+1:], inorder[inorder.index(preorder[0])+1:])


if __name__ == '__main__':
    rebuild()

