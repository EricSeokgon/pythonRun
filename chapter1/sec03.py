# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from pip._vendor.distlib.compat import raw_input


def sayMyName(name):
    print(name + " 님 안녕 하세요")
name = raw_input("당신의 이름을 입력해 주세요 : ")

sayMyName(name)
