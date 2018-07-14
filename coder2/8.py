# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 8.py

@time: 2018/7/12 下午7:02

'''


def GetNext( pNode):
    # write code here
    if pNode.right is not None:
        pNode = pNode.right
        while pNode.left:
            pNode = pNode.left
        return pNode
    else:
        while pNode.next is not None and pNode.next.left != pNode:
            pNode = pNode.next
        if pNode.next is None:
            return None
        else:
            return pNode.next

if __name__ == '__main__':
    pass

