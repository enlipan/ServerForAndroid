# coding=utf-8



index = 1
print format(index, '3')
print '{num:03d}'.format(num=index)

info = 'hhh'
print '{0: <5}'.format(info)
sh = 'hhhhhh'
sh1 = 'getNewCarCount'
so = '000000000000000000000000'
so1 = 'getNewCarShareContent'

print sh.ljust(50), sh1.ljust(30)
print so.ljust(50), so1.ljust(30)
