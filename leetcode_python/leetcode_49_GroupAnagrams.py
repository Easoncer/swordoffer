# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_49_GroupAnagrams.py

@time: 2018/6/26 下午4:26

'''


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}

        for temp in strs:
            sortedtemp = ''.join(sorted(temp))

            if sortedtemp in dic:
                dic[sortedtemp].append(temp)
            else:
                dic[sortedtemp] = [temp]

        return dic.values()


