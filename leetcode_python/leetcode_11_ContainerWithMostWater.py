# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_11_ContainerWithMostWater.py

@time: 2018/7/26 下午2:35

'''

#
#def maxArea(height):
#    """
#    :type height: List[int]
#    :rtype: int
#    """
#    res = 0
#    for i in range(len(height)-1):
#        temp = 0
#        for j in range(len(height)-1, i,-1):

#            if temp >= height[j]:
#                continue
#            else:
#                temp = height[j]
#                res = max(res, (j-i)*min(height[j], height[i]))
#    return  res

def maxArea(height):

    res = 0

    i, j = 0 ,len(height)-1

    while i < j:

        res = max(res, min(height[i], height[j])*(j-i))
        if height[i] > height[j]:
            j -= 1
        else:
            i += 1
    return res


    # for i in range(len(height)-1):
    #     temp = 0
    #     for j in range(len(height)-1, i,-1):
    #
    #         if temp >= height[j]:
    #             continue
    #         else:
    #             temp = height[j]
    #             res = max(res, (j-i)*min(height[j], height[i]))
    # return  res

if __name__ == '__main__':
    print maxArea([1,8,6,2,5,4,8,3,7])

