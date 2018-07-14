# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 13.py

@time: 2018/7/13 下午5:09

'''
def addSum(x):
    res = 0
    while x:
        res += x%10
        x = x/10
    return res

def movingCount(threshold, rows, cols):

    if threshold < 0 or rows < 0 or cols < 0:
        return 0

    stack = [(0,0)]
    count = 0
    visited = [ [0 for i in range(cols)] for j in range(rows)]

    while stack:
        i,j = stack.pop(0)

        if addSum(i) + addSum(j) <= threshold:
            count += 1

        else:
            continue

        if  i+1 < rows and visited[i+1][j] == 0:
            visited[i+1][j] = 1
            stack.append((i+1, j))
        if  j+1 < cols and visited[i][j+1] == 0:
            visited[i][j+1] = 1
            stack.append((i,j+1))
    return count


if __name__ == '__main__':
    print movingCount(5, 10, 10)

