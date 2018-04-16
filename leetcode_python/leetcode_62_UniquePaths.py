# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_62_UniquePaths.py

@time: 2018/4/13 下午12:13

'''
res = 0

def dfs(mark,step_x, step_y,m,n):
    global res
    print step_x,step_y
    #print mark
    if step_x == m-1 and step_y == n-1:
        res += 1
        print 'return '
        return

    if step_x+1 < m and mark[step_x+1][step_y] == 0 :
        mark[step_x + 1][step_y] = 1
        dfs(mark,step_x + 1, step_y,m,n)
        mark[step_x + 1][step_y] = 0

    if step_y+1 < n and mark[step_x][step_y+1] == 0 :
        mark[step_x ][step_y + 1] = 1
        dfs(mark, step_x , step_y+1,m,n)
        mark[step_x ][step_y+1] = 0


# first way dfs
def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    global res
    mark = [[0 for i in range(n)] for j in range(m)]

    mark[0][0]=1
    dfs(mark,0,0,m,n)
    print res

if __name__ == '__main__':
    uniquePaths(10,10)

