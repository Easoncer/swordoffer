# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 22.py

@time: 2018/7/15 上午11:23

'''
def findtheKtoTail(head, k):
    if not head:
        return  None
    step, i, j = 0, head, head
    while i :
        if step == k - 1:
            break
        i = i.next
        step += 1

    while  p:
        p =p.next
        q= q.next
    return q


if __name__ == '__main__':
    pass

