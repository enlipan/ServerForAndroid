# coding=utf-8

cars = list(range(1, 101))
cars2 = [car * 2 for car in cars]


# print cars2
# print cars2[0:3]
# print cars2[-2:]
# print cars[::5]

# step 步长为负数，表示从右之左，按照索引值与起始位置索引之差可以被步长整除的规律取值
print cars[::-10]

# L = ['Hello', 'World', 18, 'Apple', None]
# L = [l.lower() for l in L if isinstance(l, str)]
# print L

#
# def add(x, y, f):
#     return f(x) + f(y)
# print add(-1, 1, abs)

# def f_2(x):
#     return x**2

# 不同类型的数据的比较  -- Python3 中已修复
# In CPython2, when comparing two non-numerical objects of different types, the comparison is performed by comparing the names of the types. Since 'int' < 'string', any int is less than any string.
x = raw_input("Input Value :\n")
if x > 10:
    print "10", x, type(x)
elif x > 100:
    print "100", x, type(x)
else:
    print x, type(x)

if isinstance(x,str):
    print "str"
else:
    print type(x)