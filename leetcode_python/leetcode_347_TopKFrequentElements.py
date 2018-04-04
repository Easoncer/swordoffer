# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_347_TopKFrequentElements.py

@time: 2018/4/4 下午2:03

'''


def topKFrequent( nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    dic = {}
    for i in nums:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    tempdic = {}
    print dic
    for key, value in dic.items():
        if value in tempdic:
            tempdic[value].append(key)
        else:
            tempdic[value] = [key]
    print tempdic
    bucket = [0] * len(nums)

    for key, value in tempdic.items():
        bucket[key - 1] = value

    print bucket
    count = 0
    res = []
    for i in range(len(nums) - 1, -1, -1):
        if bucket[i]:
            count += len(bucket[i])
            res += bucket[i]
            if count == k:
                return res

if __name__ == '__main__':
    print topKFrequent([1,1,1,2,2,3], 2)

