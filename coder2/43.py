# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 43.py

@time: 2018/7/16 下午9:58

'''

# https://blog.csdn.net/yi_afly/article/details/52012593

def numberofBetweenNum(n):

    # ge wei
    if n % 10:
        count = n/10+1
    else:
        count = n/10

    round = n/10
    t = 10
    # 计算后续位

    while round :
        base = round % 10
        round /= 10

        if base > 1 :
            add = t
        elif base == 1:
            add = (n%base) + 1
        else:
            add = 0

        count += round*t+ add

        t *= 10

    return count

if __name__ == '__main__':
    print numberofBetweenNum(530)

