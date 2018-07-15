# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 25.py

@time: 2018/7/15 下午5:12

'''


def Merge(pHead1, pHead2):
    # write code here
    if pHead1 is None:
        return pHead2
    if pHead2 is None:
        return pHead1

    if pHead1.val < pHead2.val:
        merge = pHead1
        merge.next = Merge(pHead1.next, pHead2)
    else:
        merge = pHead2
        merge.next = Merge(pHead1, pHead2.next)
    return merge

if __name__ == '__main__':
    pass

