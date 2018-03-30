# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_412_FizzBuzz.py

@time: 2018/3/31 上午1:12

'''


def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    res = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            res.append('FizzBuzz')
            continue
        if i % 3 == 0:
            res.append('Fizz')
        elif i % 5 == 0:
            res.append('Buzz')
        else:
            res.append(str(i))
    return res

if __name__ == '__main__':
    pass

