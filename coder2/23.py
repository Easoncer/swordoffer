# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 23.py

@time: 2018/7/15 上午11:27

'''
def EntryNodeOfLoop( pHead):
    # write code here
    if pHead is None and pHead.next is None and pHead.next.next is None:
        return None
    p1 = pHead.next
    p2 = pHead.next.next

    while p1 != p2:
        if p1.next is not None and p2.next.next is not None:
            p1 = p1.next
            p2 = p2.next.next
        else:
            return None
    p1 = pHead

    while p1 != p2:
        if p1.next is not None and p2.next is not None:
            p1, p2 = p1.next, p2.next
    return p1

if __name__ == '__main__':
    pass

