# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_338_Counting Bits.py

@time: 2018/3/30 下午5:11

'''

def countBits(num):
    # num : int
    offset = 1
    res = [0]
    for i in range(1,num+1):

        res.append(res[i-offset] + 1)
        if i == offset:
            offset *= 2
    return  res

if __name__ == '__main__':
    print countBits(5)

