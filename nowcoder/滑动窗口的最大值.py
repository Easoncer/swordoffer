# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 滑动窗口的最大值.py

@time: 2018/6/3 下午1:20

'''

class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if size <= 0 or len(num) < size:
            return []
        res = []
        stack_list = []
        for i in range(size):
            while stack_list and num[stack_list[-1]] < num[i]:
                stack_list.pop()
            stack_list.append(i)

        for i in range(size, len(num)):
            res.append(num[stack_list[0]])
            while stack_list and num[stack_list[-1]] < num[i]:
                stack_list.pop()
            stack_list.append(i)
            if stack_list and i - stack_list[0] > size - 1:
                stack_list.pop(0)
        res.append(num[stack_list[0]])
        return res

if __name__ == '__main__':
    pass

