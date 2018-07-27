# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_200_NumberofIslands.py

@time: 2018/7/27 下午5:30

'''

def dfs(grid, i, j):
    if  i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1'  :
        return
    grid[i][j] = '#'
    dfs(grid, i - 1, j)
    dfs(grid, i, j - 1)
    dfs(grid, i + 1, j)
    dfs(grid, i, j + 1)

def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if len(grid) == 0:
        return  0

    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(grid, i, j)
                count += 1
    return count

if __name__ == '__main__':
    print numIslands([['1','1','0','0','0'],['1','1','0','0','0'],['0','0','1','0','0'],['0','0','0','1','1']])

