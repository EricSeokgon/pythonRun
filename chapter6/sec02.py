# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

my_dic = {'name': 'abc', 'year': 2015, 'age': 20}

print(my_dic.keys())
print(my_dic.values())

print(my_dic.items())
print(my_dic.clear())

print(my_dic.get('name'))
print(my_dic.get('age'))
print(my_dic.get('hello'))
# print(my_dic.['hello'])

my_dic = {'name': 'abc', 'year': 2015, 'age': 20}
print('name' in my_dic)
print('hello' in my_dic)

set1 = set([1, 2, 3, 4])
list1 = list(set1)
print(list1[3])
tuple1 = tuple(set1)
print(tuple1[2])

