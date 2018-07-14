# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 18.py

@time: 2018/7/14 下午9:43

'''
def deletdNode(head, p):
    if not head or head == p:
        return None

    if p.next:
        p.val = p.next.val
        p.next = p.next.next
    else:
        q = head
        while q.next.next:
            q = q.next
        q.next = None
    return head

if __name__ == '__main__':
    pass

