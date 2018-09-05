# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

x = 1
x = -2
x = 0

x = 23.98
x = -12.22

a = 1 + 2j
a.real
# =>실수 부분 1.0 리턴

a.imag
# =>허수 부분 2.0 리턴

a.conjugate()
# =>컬레 복소수 1-2j 리턴

abs(a)
# =>복소수 절대값 2.23606797749979 리턴

o = 0o12
# =>1*8+2*1=1-

h = 0xAB
# =>A*16+B*1=171

a = 5
b = 4

print(a + b)
print(a * b)
print(a / b)
