# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 10.py

@time: 2018/7/12 下午7:39

'''


def Fibonacci(self, n):
    # write code here
    if n == 0:
        return 0
    if n == 1:
        return 1
    temp = [0, 1]
    for i in range(2, n + 1):
        temp.append(temp[i - 1] + temp[i - 2])
    return temp[-1]

if __name__ == '__main__':
    pass

