# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 64.py

@time: 2018/7/29 下午8:21

'''
def comSum(n):
    if n == 1:
        return 1
    return n + comSum(n-1)

if __name__ == '__main__':
    print comSum(10)

