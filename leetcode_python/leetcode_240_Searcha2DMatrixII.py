# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_240_Searcha2DMatrixII.py

@time: 2018/6/27 上午11:01

'''


def searchMatrix( matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    if len(matrix) == 0:
        return False

    row = len(matrix)
    col = len(matrix[0])

    x, y = col - 1, 0
    while x > -1 and y < row:
        if matrix[y][x] > target:
            x -= 1
        elif matrix[y][x] < target:
            y += 1
        else:
            return True
    return False

if __name__ == '__main__':
    print searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20)
    #print len([])
