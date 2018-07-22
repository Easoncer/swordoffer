# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 48.py

@time: 2018/7/18 上午10:56

'''


def lengthOfLongestSubstring( s):
    # """
    # :type s: str
    # :rtype: int
    # """
    # if s == '':
    #     return 0
    # dic = {}
    # start = 0
    # max_length = 0
    # for index, char in enumerate(s):
    #     if char not in dic:
    #         dic[char] = index
    #
    #     else:
    #         if dic[char] >= start:
    #
    #             max_length = max(index - start, max_length)
    #             start = dic[char] + 1
    #
    #         dic[char] = index
    #
    # return max(max_length, index - start + 1)


    ### dp + hash method
    # if s == '':
    #     return  0
    #
    # start = 0
    # max_length = 0
    # dic = {}
    # dic[s[0]] = 0
    # dp_list = [1]
    #
    # for index , char in enumerate(s[1:]):
    #     if char not in dic:
    #         dic[char] = index
    #         dp_list.append(dp_list[index-1] + 1)
    #     else:
    #         if index - dic[char] > dp_list[index-1]:
    #             dp_list.append(dp_list[index-1] + 1)
    #         else:
    #             dp_list.append(index - dic[char])
    #     max_length = max(max_length, dp_list[-1])
    # return dp_list

    ### hash method
    if s == "":
        return 0
    start = 0
    max_length = 0
    dic = {}
    for index, char in enumerate(s):
        if char not in dic:
            dic[char] = index
        else:
            if start < dic[char]:
                start = dic[char] + 1
            max_length = max(max_length, index - start)


            dic[char] = index
        print  start
    return max(max_length, index - start +1)

if __name__ == '__main__':
    print lengthOfLongestSubstring('abba')

