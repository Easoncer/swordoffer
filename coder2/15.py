# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 15.py

@time: 2018/7/13 下午9:07

'''

def theNumberInbinary(x):
    flag = 1
    count = 0
    while flag < pow(2,32):
        if flag & x :
            count += 1
        flag = flag << 1
    return count

if __name__ == '__main__':
    print theNumberInbinary(7)

