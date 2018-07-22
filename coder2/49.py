# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 49.py

@time: 2018/7/22 下午9:55

'''


def GetUglyNumber( index):
    # write code here
    if index == 0:
        return 0
    a = [1]
    k2 = 0
    k3 = 0
    k5 = 0
    for i in range(index):
        a.append(min(a[k2] * 2, a[k3] * 3, a[k5] * 5))
        if a[-1] == a[k2] * 2:
            k2 += 1
        if a[-1] == a[k3] * 3:
            k3 += 1
        if a[-1] == a[k5] * 5:
            k5 += 1
    return a[index - 1]


if __name__ == '__main__':
    print GetUglyNumber(3)

