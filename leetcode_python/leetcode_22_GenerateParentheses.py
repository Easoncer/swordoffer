# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_22_GenerateParentheses.py

@time: 2018/4/5 下午4:01

'''
def backtrack(res, str, start, end, max_num):
    if len(str) == 2*max_num:
        res.append(str)
        return

    if start < max_num:
        backtrack(res, str+'(', start+1, end , max_num)
    if end  < start:
        backtrack(res, str+')', start, end +1,max_num)


def generateParenthesis( n):
    """
    :type n: int
    :rtype: List[str]
    """
    res = []
    str = ''
    start = 0
    end = 0

    backtrack(res, str, start, end, n)

    return res
if __name__ == '__main__':
    print generateParenthesis(3)

