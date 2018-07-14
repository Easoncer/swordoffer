# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 16.py

@time: 2018/7/14 下午5:18

'''

# def comPower(base, exp):
#     res = 1
#     for i in range(exp):
#         res *= base
#     return res

def comPower(base, exp):
    if exp == 1:
        return base

    if exp % 2 :
        res = comPower(base, exp/2)

        return res*res *base
    else:
        res = comPower(base, exp/2)
        return  res *res



def power(base, exp):
    if exp == 0:
        return 1
    if exp == 1:
        return base

    absexp = abs(exp)

    res = comPower(base, absexp)

    if exp < 0:
        return 1.0/res
    return res

if __name__ == '__main__':
    print power(2,2)

