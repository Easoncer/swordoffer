# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 6.py

@time: 2018/7/12 下午5:27

'''
class linkNode:
    def __init__(self, val):
        self.next = None
        self.data = val

def printListFromTailToHead( listNode):
    # if listNode is None:
    #     return []
    # stacklist = []
    # while listNode:
    #     stacklist.append(listNode.val)
    #     listNode = listNode.next
    # stacklist.reverse()
    # return stacklist

    if not listNode:
        return []

    as_stack = []

    while listNode:
        as_stack.append( listNode.data)
        listNode = listNode.next

    as_stack.reverse()
    return as_stack

if __name__ == '__main__':
    head = linkNode(1)
    p = linkNode(3)
    head.next = p
    print printListFromTailToHead(head)


