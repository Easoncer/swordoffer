# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_438_FindAllAnagramsinaString.py

@time: 2018/8/17 下午8:15

'''
def findAnagrams( s, p):
    '''
    :param s: string s
    :param p: non-empty string p

    slide-windows
    '''
    from collections import defaultdict
    left, right = 0, 0
    count = len(p)
    res = []
    mark = {}
    for i in p:
        if i in mark:
            mark[i] += 1
        else:
            mark[i] = 1

    while right < len(s):
        if mark[s[right]] >= 1:
             count -= 1
        mark[s[right]] -= 1
        right += 1
        if count == 0:
            res.append(left)
         # 字串长度和p相等，begin向前移动
        if right - left == len(p):
            print mark , count
            if mark[s[left]] >= 0:
                count += 1
            # begin向前移动
            mark[s[left]] += 1
            left += 1

    return res

if __name__ == '__main__':
    print findAnagrams('cbabac','abc')