# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 二叉树的下一个结点.py

@time: 2018/5/30 下午4:56

'''


def GetNext( pNode):
    # write code here
    if pNode.right is not None:
        pNode = pNode.right
        while pNode.left:
            pNode = pNode.left
        return pNode
    else:
        if pNode.next is None:
            return None
        if pNode.next.left is pNode:
            return pNode.next
        else:
            while pNode.next is not None and pNode.next.left != pNode:
                pNode = pNode.next
            if pNode.next is None:
                return None
            else:
                return pNode.next

if __name__ == '__main__':
    pass

