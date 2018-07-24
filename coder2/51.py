# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 51.py

@time: 2018/7/23 下午3:33

'''

def merge(a, b, count ):
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            count += 1
            c.append(b[h])
            h += 1

    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            count += 1
            c.append(i)

    return (c,count)


def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    middle = len(lists)/2
    left = merge_sort(lists[:middle])

    right = merge_sort(lists[middle:])
    print left,right
    count = 0
    (c, count) = merge(left, right,count)
    print count
    return c

if __name__ == '__main__':

    print merge_sort([7,5,6,4])

