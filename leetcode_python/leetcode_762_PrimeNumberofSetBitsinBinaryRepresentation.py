# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_762_PrimeNumberofSetBitsinBinaryRepresentation.py

@time: 2018/4/2 下午2:14

'''


def countPrimeSetBits( L, R):
    """
    :type L: int
    :type R: int
    :rtype: int
    """
    count = 0
    for i in range(L,R+1):
        temp = bin(i)[2:].count('1')
        primelist = [2,3,5,7,11,13,17,19]
        if temp in primelist:
            print temp
            count += 1
    return count

if __name__ == '__main__':
    print countPrimeSetBits(10,15)

