# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 不用加减乘除做加法.py

@time: 2018/5/28 下午9:29

'''


def Add( num1, num2):
    # write code here
    res = num1
    while num2:
        num1, num2= num1 ^ num2, (num1 & num2) << 1
        res = num1 ^ num2
    return res


if __name__ == '__main__':
    print Add(11, 10)

