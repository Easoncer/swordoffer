# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_139_WordBreak.py

@time: 2018/8/19 上午11:08

'''

# DFS Time Exceeded

def compareStr(str, dicstr):
    i = 0
    if len(dicstr) > len(str):
        return (False, 0)

    for i in range(len(dicstr)):
        if str[i] != dicstr[i]:
            return (False, 0)
    return (True, i+1)


def dfs(str, worddic, index, result):

    if result:
        return result

    if index == len(str):
        return True

    for i in worddic:
        res = compareStr(str[index:], i)
        if res[0]:
            temp = dfs(str, worddic, index + res[1], result)
            result =  result or temp
    return result


def wordBreak( s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    result = False
    return dfs(s, wordDict, 0, result)

if __name__ == '__main__':
    print wordBreak("aaaaaaa",["aaaa", "aa"])

