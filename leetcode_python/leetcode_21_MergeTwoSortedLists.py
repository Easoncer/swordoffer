# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_21_MergeTwoSortedLists.py

@time: 2018/4/18 下午12:28

'''
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

def mergeTwoLists( l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    h = temp = ListNode(0)

    while l1 and l2:
        if (l1.val > l2.val):
            temp.next = l2
            l2 = l2.next
        else:
            temp.next = l1
            l1 = l1.next
        temp = temp.next
    temp.next = l1 or l2

    return h.next


if __name__ == '__main__':
    pass

