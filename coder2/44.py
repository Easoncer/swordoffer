# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 44.py

@time: 2018/7/17 下午1:52

'''
def digitalIndex(n):
    if n < 10:
        return n
    res = 9
    base = 2
    mul = 90

    while n >= res  and n < res + base*mul:
        res += base*mul
        base += 1
        mul *= 10

    base -= 1
    mul /= 10
    res -= base*mul

    offset = n - res

    p, q = (offset-1)/base, (offset-1)%base
    print base

    return int(str(pow(10, base) + p)[q])

if __name__ == '__main__':
    print digitalIndex(11)

