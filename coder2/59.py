# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 59.py

@time: 2018/7/26 下午4:34

'''
def maxInWindows(templist, size):
    queue = []
    res = []
    temp = templist[0]

    queue.append(0)
    for i in range(1,size):
        if templist[queue[-1]] > templist[i]:
            queue.append(i)
        else:
            while queue and templist[queue[-1]] <= templist[i]:
                queue.pop(-1)
            queue.append(i)

    res.append(templist[queue[0]])

    for i in range(size, len(templist)):
        if i - queue[0] >= size:
            queue.pop(0)

        if templist[queue[-1]] > templist[i]:
            queue.append(i)
        else:
            while queue and templist[queue[-1]] <= templist[i]:
                queue.pop(-1)
            queue.append(i)
        res.append(templist[queue[0]])

    return res


if __name__ == '__main__':
    print maxInWindows([2,3,4,2,6,2,5,1], 3)

