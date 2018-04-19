# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_48_RotateImage.py

@time: 2018/4/18 上午12:56

'''


def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i,len(matrix)):

            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    return matrix

if __name__ == '__main__':
    print rotate([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

