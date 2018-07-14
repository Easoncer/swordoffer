# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 17.py

@time: 2018/7/14 下午8:48

'''
def dfs(step, mark, temp_list,res):
    if step == len(mark):
        print res
        return

    for i in range(len(mark)):
        if mark[i] == 0:
            res[step] = temp_list[i]
            mark[i] = 1
            dfs(step+1, mark, temp_list, res)
            mark[i] = 0


def perumate(list_temp):

    mark = [0 for i in range(len(list_temp))]
    res = [0 for i in range(len(list_temp))]

    dfs(0, mark, list_temp, res)


if __name__ == '__main__':
    perumate(['a','s','d','f'])

