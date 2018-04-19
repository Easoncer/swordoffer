# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_96_UniqueBinarySearchTrees.py

@time: 2018/4/18 上午12:06

'''


def numTrees( n):
    """
    :type n: int
    :rtype: int
    """
    temp = [1]
    for i in range(1, n + 1):
        temp.append(sum([temp[j]*temp[i-j-1] for j in range(i)]))
    return temp

if __name__ == '__main__':
    print numTrees(6)

