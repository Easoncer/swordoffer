# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 56_2.py

@time: 2018/7/25 下午10:34

'''

def findNumberOnce(temp):


    res = [0 for i in  range(32)]
    for i in temp:
        count = 31
        flag = 1
        while count >= 0:
            num = flag&i
            if num:
                res[count] += 1
            flag = flag << 1
            count -= 1
    r = 0
    print res
    for i in range(32):
        r = r << 1
        r += res[i]%3
    return r


if __name__ == '__main__':
    print findNumberOnce([1,2,2,2,1,1,-3])

