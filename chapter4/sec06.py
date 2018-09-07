# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

a = "I love python!"
print(a.count('o'))
print(a.find('v'))
print(a.index('p'))

print(a.find('x'))  # find는 찾는 문자열이 없으면 -1
# print(a.index('x')) index는 문자열이 없으면 오류

a = " ".join("abcde")
print(a)
b = "1".join("abcde")
print(b)
c = "python".upper()
print(c)
d = "HELLO".lower()
print(d)
e = "blue".replace('b', 'g')
print(e)

f = "Hello world I'm python".split(" ")
print(f)

g = "python".split('th')
print(g)


