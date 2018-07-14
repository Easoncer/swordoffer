# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 6.py

@time: 2018/7/12 下午5:27

'''


def printListFromTailToHead( listNode):
    # write code here
    if listNode is None:
        return []
    stacklist = []
    while listNode:
        stacklist.append(listNode.val)
        listNode = listNode.next
    stacklist.reverse()
    return stacklist

if __name__ == '__main__':
    pass

