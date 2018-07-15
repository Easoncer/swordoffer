# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 19.py

@time: 2018/7/14 下午10:51

'''
def match(s, pattern):
    if not s  and not pattern:
        return True

    if not s or not pattern:
        return  False

    if len(pattern) > 1 and pattern[1] == '*':
        if s and s[0] != pattern[0] and pattern[0] != '.' \
                                                      '':
            return match(s, pattern[2:])
        if s and (s[0] == pattern[0] or pattern[0] == '.'):
            return  match(s, pattern[2:]) or match(s[1:], pattern)
    elif  (s[0] == pattern[0] or pattern[0] == '.'):
        return match(s[1:], pattern[1:])
    return False


if __name__ == '__main__':
    print match('aaa','aa.a')
