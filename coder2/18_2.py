# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 19.py

@time: 2018/7/14 下午9:45

'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteDuplication(pHead):

    if not pHead:
        return None

    p, p.next = ListNode(0), pHead

    reNode = p

    while p.next:
        if p.next.next and p.next.val  == p.next.next.val:
            while p.next.next and p.next.val  == p.next.next.val:
                p.next = p.next.next
            p.next = p.next.next

        else:
            p = p.next
    return reNode.next



if __name__ == '__main__':
    pass

