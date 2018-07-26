# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_17_LetterCombinationsofaPhoneNumber.py

@time: 2018/7/26 下午3:15

'''


def letterCombinations( digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    return combineLetter('23',"",[])

def combineLetter(digits,s,res):
    mapdic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'ghl', '6': 'mno', '7': 'qprs', '8': 'tuv', '9': 'wxyz'}
    if digits == "":
        res.append(s)
        return

    for i in mapdic[digits[0]]:
        combineLetter(digits[1:], s+i, res)
    return res

if __name__ == '__main__':
    print combineLetter('23',"",[])

