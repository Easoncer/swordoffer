# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_463_IslandPerimeter.py

@time: 2018/3/31 下午5:23

'''


def islandPerimeter( grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    上下两列或者左右两列异或为1的则表示出现了边界
    """
    tri_grid = []
    num = len(grid)
    for i in range(len(grid[0])):
        tri_grid.append([grid[j][i] for j in range(len(grid))])
    print tri_grid

    res = grid[0].count(1) + grid[-1].count(1)+ tri_grid[0].count(1)+tri_grid[-1].count(1)

    for i in range(len(grid)-1):
        res += sum([sum(j)%2 for j in zip(grid[i],grid[i+1])])

    for i in range(len(grid[0])-1):
        res += sum([sum(j) % 2 for j in zip(tri_grid[i], tri_grid[i + 1])])

    return res



if __name__ == '__main__':
    print islandPerimeter([[1],[0]])

