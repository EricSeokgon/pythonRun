# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

a = [1, 2]
b = ['a', 'b', 'c']
print(a + b)
print(a * 4)

my_list = [1, 2, 3, 4, 5]
print(my_list[0])
print(my_list[3])
print(my_list[0] + my_list[3])

my_list = [1, 2, ['a', 'b'], 'python']
print(my_list[2])
print(my_list[2][0])
print(my_list[2][1])

a = [1, 2, 3, 4, 5]
print(a[1:4])
print(a[:3])
print(a[2:])

a[2] = 'hi'
print(a)

a = [1, 6, 5, 3, 4, 2]

print(a.index(6))
print(a.append(7))
print(a.append([8, 9]))

print(a.pop())
print(a.sort())
print(a.remove(6))
print(a.insert(0, [7, 1]))
print(a.remove(6))
