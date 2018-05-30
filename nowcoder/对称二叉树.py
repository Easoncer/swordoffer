# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 对称二叉树.py

@time: 2018/5/30 下午5:05

'''


def isSymmetrical( pRoot):
    # write code here
    def isTest(leftNode, rightNode):
        if leftNode is None and rightNode is None:
            return True
        if leftNode is None or rightNode is None:
            return False
        if leftNode.val == rightNode.val:
            return isTest(leftNode.right, rightNode.left) and isTest(leftNode.left, rightNode.right)
        else:
            return False

    if pRoot is None:
        return True
    return isTest(pRoot, pRoot)

if __name__ == '__main__':
    pass

