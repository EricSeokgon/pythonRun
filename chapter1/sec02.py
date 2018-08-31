# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from pip._vendor.distlib.compat import raw_input

print("성별을 입력해주세요 male 혹은 female : ")
gender = raw_input()

if(gender == "male"):
    print("남자입니다.")
elif(gender == "female"):
    print("여자입니다.")
else:
    print("알 수 없는 성별입니다.")

