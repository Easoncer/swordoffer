# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_647_PalindromicSubstrings.py

@time: 2018/4/2 下午2:23

'''


def countSubstrings( s):
    """
    :type s: str
    :rtype: int
    """
    res = 0
    res += len(s)
    # BAB
    for i in range(1, len(s) - 1):
        j = 1
        while i + j < len(s) and i - j >= 0:
            if s[i - j:i] == s[i + 1:i + j + 1][::-1]:
                res += 1
                j += 1
            else:
                break

    # ABBA
    for i in range(0, len(s) - 1):

        if s[i] == s[i + 1]:
            res += 1
            j = 1
            while i - j >= 0 and i + 1 + j < len(s):
                if s[i - j:i + 1] == s[i + 1:i + j + 2][::-1]:
                    res += 1
                    j += 1
                else:
                    break

    return res

if __name__ == '__main__':
    pass

