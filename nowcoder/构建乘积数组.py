# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 构建乘积数组.py

@time: 2018/5/29 下午3:08

'''


def multiply( A):
    # write code here
    res, temp = [1], 1
    for i in A[:-1]:
        temp *= i
        res.append(temp)
    print res

    temp = 1
    for index in range(len(A) - 1, 0, -1):
        temp *= A[index]
        res[index-1] *= temp
    return res


if __name__ == '__main__':
    print multiply( [1, 2, 3, 4, 5])

