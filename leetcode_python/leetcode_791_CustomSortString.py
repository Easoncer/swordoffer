# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_791_CustomSortString.py

@time: 2018/3/30 下午9:51

'''


def customSortString( S, T):
    resultnum = [0 for i in range(26)]

    str = ''
    for i in T:
        if i in S:
            resultnum[ord(i) - 97] += 1
        else:
            str += i

    for i in S:
        str += i * resultnum[ord(i) - 97]


    #return [ i*resultnum[ord(i)-97] for i in


    return str


if __name__ == '__main__':
    print customSortString('dfag','aaadfgh')

