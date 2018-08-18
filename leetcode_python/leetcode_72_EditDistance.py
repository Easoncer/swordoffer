# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_72_EditDistance.py

@time: 2018/8/18 下午4:36

'''
# 双序列动态规划问题

def minDistance(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    w1, w2 = len(word1), len(word2)
    dp = [[0 for i in range(w1+1)] for j in range(w2+1)]

    for i in range(1, w1+1):
        dp[0][i] = i

    for j in range(1, w2+1):
        dp[j][0] = j

    for i in range(1, w2+1):
        for j in range(1, w1+1):
            if word1[j-1] == word2[i-1]:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]+1, dp[i][j-1]+1)
            if word1[j - 1] != word2[i - 1]:
                dp[i][j] = min(dp[i-1][j-1]+1, dp[i-1][j]+1, dp[i][j-1]+1)
    return dp[w2][w1]

if __name__ == '__main__':
    print minDistance('horse','ros')

