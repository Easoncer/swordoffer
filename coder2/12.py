# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 12.py

@time: 2018/7/12 下午11:01

'''

def isRight(matrix, vistited, rows, cols, i, j,path):

    # if path == "":
    #     print "here"
    #     return True

    f1, f2, f3, f4 = False, False, False, False

    if matrix[i][j] == path[0]:

        if path[1:] == "":
            return True

        vistited[i][j] = 1

        if j+1 < cols and vistited[i][j+1] == 0:
            print "col+1"
            vistited[i][j+1] = 1
            f1 = isRight(matrix, vistited, rows, cols, i, j+1, path[1:])
            vistited[i][j+1] = 0

        if j-1 >= 0 and vistited[i][j-1] == 0:
            print "col-1"
            vistited[i][j-1] = 1
            f2 = isRight(matrix, vistited, rows, cols, i, j-1, path[1:])
            vistited[i][j-1] = 0

        if i-1 >= 0 and vistited[i-1][j] == 0:
            print "row-1"
            vistited[i-1][j] = 1
            f3 = isRight(matrix, vistited, rows, cols, i-1, j, path[1:])
            vistited[i-1][j] = 0

        if i+1 < rows and vistited[i+1][j] == 0:
            print "row+1"
            vistited[i+1][j] = 1
            f4 = isRight(matrix, vistited, rows, cols, i+1, j, path[1:])
            vistited[i+1][j] = 0

        vistited[i][j] = 0
    return f1 or f2 or f3 or f4

def hasPath( matrix, rows, cols, path):
    vistited = [[0 for i in range(cols)]  for j in range(rows) ]

    for i in range(rows):
        for j in range(cols):
            if isRight(matrix, vistited, rows, cols,i, j, path):
                return True
    return False


if __name__ == '__main__':
    #print  hasPath([['a','a','a','a'],['a','a','a','a'],['a','a','a','a']],3,4,'aaaaaaaaaaaa')
    print hasPath([['a','b','c','e'],['s','f','c','s'],['a','d','e','e']],3,4,'abcced')

