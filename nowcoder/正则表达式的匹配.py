# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 正则表达式的匹配.py

@time: 2018/5/29 下午3:31

'''


def match(s, pattern):
    if s == pattern:
        return True
    if len(pattern) > 1 and pattern[1] == '*':
        if s and (s[0] == pattern[0]  or pattern[0] == '.'):
            # match 0 times and many times
            return match(s, pattern[2:]) or match(s[1:], pattern)
        else:
            # '*'  match 0 times
            return match(s, pattern[2:])
    # not contains the '*'
    elif s and pattern and (s[0] == pattern[0] or pattern[0]=='.'):
        return  match(s[1:], pattern[1:])
    return  False


if __name__ == '__main__':
    print match('abcd','abc.')

