# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 57_2.py

@time: 2018/7/26 下午4:10

'''

def FindContinusSequence(sum):
    mid = (sum+1)/2
    if sum == 1 or sum == 2:
        return None
    if sum == 3:
        return [1,2]

    left, right= 1, 2

    res = []
    temp = left + right

    while right <= mid:
        if temp == sum:
            res.append([i for i in range(left, right+1)])
            temp -= left
            left += 1
        elif temp > sum :
            temp -= left
            left += 1
        else:
            right += 1
            temp += right
    return res


if __name__ == '__main__':
    print FindContinusSequence(15)

