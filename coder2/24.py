# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 24.py

@time: 2018/7/15 下午4:23

'''


def ReverseList( pHead):
    # write code here
    stack_list = []
    if not pHead:
        return None
    # p, p.next = ListNode(0), pHead
    while pHead:
        stack_list.append(pHead)
        pHead = pHead.next

    # return pHead
    p = stack_list.pop(-1)

    q = p
    while stack_list:
        temp = stack_list.pop(-1)
        temp.next = None
        p.next = temp
        p = p.next

    return q

if __name__ == '__main__':
    ReverseList(head)

