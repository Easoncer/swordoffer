# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 数组中重复的数字.py

@time: 2018/5/29 上午1:44

'''

def duplicate( numbers, duplication):
    # write code here
    duplication[0] = -1
    for index, value in enumerate(numbers):
        if numbers[abs(value)] >= 0:
            numbers[abs(value)] *= -1
        else:
            duplication[0] = abs(value)
            return True
    return False

if __name__ == '__main__':
    pass

