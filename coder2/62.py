# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 62.py

@time: 2018/7/29 下午7:54

'''
def lastRemaining(n, m):
    temp = [i for i in range(n)]
    res = 0
    shift = 0
    while temp:
        del_index = (m -1 + shift) % n
        res = temp.pop(del_index)
        #print res
        n -= 1
        shift = del_index
    return res

if __name__ == '__main__':
    print lastRemaining(5,3)

