# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_413_ArithmeticSlices.py

@time: 2018/4/2 下午3:49

'''


def numberOfArithmeticSlices( A):
    """
    :type A: List[int]
    :rtype: int
    """

    num = len(A)
    if num < 3:
        return 0
    dp = [0 for i in range(num)]
    res = 0
    if A[2] - A[1] == A[1] - A[0]:
        dp[2] = 1
        res += 1
    # dp[i] means the number of arithmetic slices ending with A[i]
    for i in range(3, num):
        if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
            dp[i] = dp[i - 1] + 1
        res += dp[i]
    return res


if __name__ == '__main__':
    pass

