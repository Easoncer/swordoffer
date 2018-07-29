# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 63.py

@time: 2018/7/29 下午8:11

'''

# leetcode 121


def maxDiff(temp):
    res = 0
    if not temp:
        return  0
    tempmin = temp[0]
    for i in temp[1:]:
        if i > tempmin:
            res = max(res, i- tempmin)
        else:
            tempmin = i
    return  res

if __name__ == '__main__':
    print maxDiff([9,11,8,5,7,12,16,14])

