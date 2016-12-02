#coding=utf-8

import re


"""
r 前缀表示 纯字符，不带转义等字符

r 后跟 \n 表示 一个 \ 反斜杠 + 一个 n 字符

正则表达式
|  分枝条件
\w 字母数字
\d  数字
\s  空格
^   行首
$   行尾
()  分组


"""

if __name__ == '__main__':
    email = raw_input()
    if re.match(r'^[0-9a-zA-Z\_\.]+@[0-9a-zA-Z\_\.]+\.com$', email):
        print 'Bingo!!! %s' % email
    else:
        print 'email is unValidate ---X %s' % email