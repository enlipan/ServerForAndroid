# coding=utf-8
import unicodedata


def wide_chars(s):
    return sum(unicodedata.east_asian_width(x) == 'W' or unicodedata.east_asian_width(x) == 'A' for x in s)


index = 1
print format(index, '3')
print '{num:03d}'.format(num=index)

info = 'hhh'
print '{0: <5}'.format(info)
sh = '呵呵呵呵呵呵好呀呀呀呀'
sh1 = 'getNewCarCount'
so = '呵呵呵呵呵呵好'
so1 = 'getNewCarShareContent'

# print("|%*s|%*s|" % (24-wide_chars(unicode(sh)), sh1, 4-wide_chars(unicode(so)), so1))

