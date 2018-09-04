# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from pip._vendor.distlib.compat import raw_input

age = input("나이를 입력해 주세요: ")
#=> 20 입력
print(age)
#=> 20 출력

name = raw_input("이름을 입력해 주세요 : ")
#=>홍길동 입력
print(name)
#=>홍길동 출력