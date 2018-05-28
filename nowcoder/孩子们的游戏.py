# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 孩子们的游戏.py

@time: 2018/5/28 下午7:04

'''


def LastRemaining_Solution( n, m):
    # write code here
    if m==0 or n == 0:
        return  -1
    queue_list = range(n)
    while len(queue_list) > 1:
        temp = m - 1
        while temp:
            number = queue_list.pop(0)
            queue_list.append(number)
            temp -= 1
        queue_list.pop(0)
    return queue_list[0]


if __name__ == '__main__':
    print LastRemaining_Solution(5,1)

