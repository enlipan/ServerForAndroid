# coding=utf-8


dict = {}
# key => string numbers  tuples
# strings and tuples work cleanly since they are immutable(不可变对象)，如List 对象可以添加元素
dict['a'] = 'alpha'
print(dict['a'])

dict['b'] = 'beta'
print(dict)

# 利用 字典合理组织数据
dict['aa'] = 'alBe'
for key in sorted(dict.keys()):
    print(key, dict[key])

# string format %
s = '%(aa)s %(b)s' % dict
print(s)
