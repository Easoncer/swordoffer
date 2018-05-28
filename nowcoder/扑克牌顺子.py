# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 扑克牌顺子.py

@time: 2018/5/28 下午4:49

'''


def IsContinuous( numbers):
    # write code here
    if not numbers:
        return False
    numbers.sort()
    count = 0
    zero_number = 0
    for index, value in enumerate(numbers[:-1]):
        if value != 0:
            if numbers[index + 1] == value:
                return False
            zero_number += numbers[index + 1] - value -1
        else:
            count += 1
    return (zero_number <= count)

if __name__ == '__main__':
    print IsContinuous([1,3,2,6,4])
