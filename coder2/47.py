# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 47.py

@time: 2018/7/17 下午2:51

'''
def getMaxValue(mat):
    row = len(mat)
    col = len(mat[0])

    temp_mat = [[0 for i in range(col)] for j in range(row)]

    #temp_mat[0] = mat[0][:]
    temp_mat[0][0] = mat[0][0]

    # for i in range(1,col):
    #     temp_mat[0][i] = temp_mat[0][i-1]


    for i in range(row):
        for j in range(col):
            if i == 0 :
                temp_mat[i][j] = mat[i][j] + temp_mat[i][j-1]
            if j == 0:
                temp_mat[i][j] = mat[i][j] + temp_mat[i-1][j]
            temp_mat[i][j] = mat[i][j] + max(temp_mat[i][j-1], temp_mat[i-1][j])
    return temp_mat


if __name__ == '__main__':
    print getMaxValue([[1,10,3,8],[12,2,9,6],[5,7,4,11],[3,7,16,5]])

