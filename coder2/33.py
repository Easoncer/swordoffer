# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 33.py

@time: 2018/7/15 下午10:23

'''

def verifySquence(seq):
    if len(seq) == 0:
        return False

    if len(seq) == 1:
        return True

    for i in range(len(seq)-1):
        if seq[i] > seq[-1]:
            break

    for j in range(i,len(seq)-1):
        if seq[j] < seq[-1]:
            return False

    return  verifySquence(seq[:i]) and verifySquence(seq[i:-1])


if __name__ == '__main__':
    print verifySquence([3,5.5,5,7,6,9,11,10,8])

