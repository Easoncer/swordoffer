# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 57.py

@time: 2018/7/26 下午4:04

'''
def FindNumberWithSum(data, sum):
    if not data:
        return None
    i,j = 0, len(data)-1
    while i < j:
        if data[i]+data[j] == sum:
            return (data[i], data[j])
        elif data[i] + data[j] >sum:
            j -= 1
        else:
            i += 1
    return -1
if __name__ == '__main__':
    print FindNumberWithSum([1,2,3,4,5],10)

