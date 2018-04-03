# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_526_BeautifulArrangement.py

@time: 2018/4/2 下午4:24

'''
def dfs(step, mark, nums,res):

    if step == len(nums):
        print 'num',nums

        #res.append(nums)
        #print res
        #res.append(nums)
        # difference deep copy and shallow copy
        res.append(nums[:])
        print 'res', res
        return

    for i in range(len(nums)):
        if mark[i] == 0:

            if (i+1) % (step+1) == 0 or (step+1) % (i+1) ==0 :
                mark[i] = 1
                nums[step] = i + 1
                dfs(step+1, mark, nums, res)
                mark[i] =0
            else:
                continue
                #dfs(step,mark,nums)
    return



def countArrangement( N ):
    """
    :type N: int
    :rtype: int
    """
    mark = [0 for i in range(N)]
    nums = [0 for i in range(N)]
    res = []
    dfs(0, mark, nums ,res)
    print res



if __name__ == '__main__':
    countArrangement(2)
    #print len(res)

