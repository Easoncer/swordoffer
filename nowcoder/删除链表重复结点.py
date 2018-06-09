# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 删除链表重复结点.py

@time: 2018/6/9 下午9:20

'''

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead is None:
            return None
        p, p.next = ListNode(0), pHead
        reNode = p
        while p.next:
            if p.next.next and p.next.val == p.next.next.val:
                while p.next.next and p.next.val == p.next.next.val:
                    p.next = p.next.next
                p.next = p.next.next
            else:
                p = p.next
        return reNode.next

if __name__ == '__main__':
    pass

