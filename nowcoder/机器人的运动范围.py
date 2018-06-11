# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 机器人的运动范围.py

@time: 2018/6/11 上午9:41

'''

def intSum(x):
    res = 0
    while x :
        res += x %10
        x= x/10
    return  res

def movingCount( threshold, rows, cols):
    if rows < 0 or cols < 0 or threshold <0:
        return 0
    mark = [ [0 for i in range(cols)] for j in range(rows)]

    queuelist = [(0,0)]
    count = 0
    while queuelist:
        x, y = queuelist.pop(0)

        count += 1

        if x+1 < cols  and mark[y][x+1] == 0 and intSum(x+1)+intSum(y) <= threshold:
            queuelist.append((x+1,y))
            mark[y][x+1] = 1

        if y+1 < rows  and mark[y+1][x] == 0 and intSum(x)+intSum(y+1) <= threshold:
            queuelist.append((x,y+1))
            mark[y+1][x] = 1

    return  count

if __name__ == '__main__':
    print movingCount(10, 1,100)

