# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 表示数值的字符串.py

@time: 2018/5/29 下午5:05

'''


def isNumeric( s):
    two_part = s.split('.')
    # contain the point part
    if s == None :
        return False
    #alist = [st.lower() for st in s]
    lowstr = s.lower()
    if 'e' in s.lower():
        indexE = lowstr.index('e')
        front = lowstr[:indexE]
        behind = lowstr[indexE+1:]
        if '.' in behind or len(behind) == 0:
            return False
        return scanDigit(front) and scanDigit(behind)
    else:
        print "not e"
        return  scanDigit(lowstr)

def scanDigit(s):
    dotNum = 0
    str_list = ['1','2','3','4','5','6','7','8','9','0','+','-','.']
    for index ,value in enumerate(s):
        if value not in str_list:
            return False
        if value == '.':
            dotNum += 1

        if value in '+-' and index != 0:
            return  False

    if dotNum > 1:
        return  False
    return  True


if __name__ == '__main__':
    print isNumeric('1.2.3')
