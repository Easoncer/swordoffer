# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 14.py

@time: 2018/7/13 下午8:32

'''

def maxMuli(n):
    if n < 1 :
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    temp = [0,1,2,3]

    for i in range(4,n+1):
        temp_max = 0
        for j in range(1,i):
            temp_max = max(temp_max, temp[j]*temp[i-j])
        temp.append(temp_max)
    return temp


if __name__ == '__main__':
    print maxMuli(8)

