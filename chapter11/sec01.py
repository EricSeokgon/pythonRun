# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

f = open("파일 경로", 'w')
f.close()

# f.open("새파일.txt", 'w')
# f.close()

f = open("write.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

A = [1, 7, 3, 6]
f = open("my_list.txt", 'w')
for i in A:
    A.sort()
    list = "%d\n"%i
    f.write(list)
f.close()