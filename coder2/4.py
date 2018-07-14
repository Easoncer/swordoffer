# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 4.py

@time: 2018/7/12 下午3:31

'''

def find(matrix, key):
    if len(matrix) == 0:
        return False
    allrow = len(matrix[0])-1
    row, col = 0, len(matrix) - 1

    while row <= allrow and col >=0 :
        if matrix[row][col] > key:
            col -= 1
        elif matrix[row][col] < key:
            row += 1
        else:
            return True

    return False

if __name__ == '__main__':
    print find([[1,2,8,9], [2,4,9,12], [4,7,10,13],[6,8,11,15]],7)

