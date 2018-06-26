# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_560_SubarraySumEqualsK.py

@time: 2018/6/26 下午4:13

'''


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        tempdic = {}
        tempdic[0] = 1
        ressum = 0
        res = 0
        for i in nums:
            ressum += i

            if ressum - k in tempdic:
                res += tempdic[ressum - k]

            if ressum in tempdic:
                tempdic[ressum] += 1
            else:
                tempdic[ressum] = 1

        return res

if __name__ == '__main__':
    pass

