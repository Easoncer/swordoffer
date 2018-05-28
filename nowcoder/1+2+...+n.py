# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 1+2+...+n.py

@time: 2018/5/28 下午9:28

'''


def Sum_Solution( n):
    # write code here
    if n == 1:
        return 1
    return Sum_Solution(n - 1) + n


if __name__ == '__main__':
    pass

