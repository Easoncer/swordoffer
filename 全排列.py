# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 全排列.py

@time: 2018/3/30 下午4:14

'''
def dfs(step, mark, number):
    if step == n+1:
        print number[1:]
        return

    for i in range(1, n+1):
        if mark[i] == 0:
            number[step] = i
            mark[i] = 1
            dfs(step+1, mark, number)
            mark[i] = 0
    return

def Permutations(n):
    # all the numbers
    number = range(0,n+1)
    # whether used
    mark = [0 for i in range(0,n+1)]
    dfs(1,mark, number)

if __name__ == '__main__':
    n = 5
    Permutations(n)