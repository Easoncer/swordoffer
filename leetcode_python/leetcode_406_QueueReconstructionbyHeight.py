# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_406_QueueReconstructionbyHeight.py

@time: 2018/4/1 下午9:15

'''


def reconstructQueue( people):
    """
    :type people: List[List[int]]
    :rtype: List[List[int]]
    """

    pdic, height, res = {}, [], []

    for index in range(len(people)):
        if people[index][0] in pdic:
            pdic[people[index][0]].append((people[index][1], index))
        else:
            pdic[people[index][0]] = [(people[index][1], index)]
            height.append(people[index][0])

    height.sort(reverse=True)

    for i in height:
        pdic[i].sort()
        for j in pdic[i]:
            res.insert(j[0], people[j[1]])
    return res



if __name__ == '__main__':
    pass

