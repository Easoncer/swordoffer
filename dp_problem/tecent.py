# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: tecent.py

@time: 2018/4/5 下午9:53

'''
def findPathtoNN(n):
    '''
    :param n: list[list[]]
    :return int n :
    '''
    mark_list = [[0]*n for i in range(n)  ]

    mark_list[0][0] = 1
    for i in range(n):
        for j in range(n):
            if i == 0 and j==0:
                continue
            if i <= j:
                rowsum = sum([mark_list[row_i][j] for row_i in range(i)])
                colsum = sum([mark_list[i][col_j] for col_j in range(j)])
                mark_list[i][j] = rowsum+colsum
                mark_list[j][i] = mark_list[i][j]
    return mark_list

if __name__ == '__main__':
    print findPathtoNN(4)

