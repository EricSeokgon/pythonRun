# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from pip._vendor.distlib.compat import raw_input

color = input("가장 좋아하는 색은?")
# =>"파랑색" 입력
print(color)
# =>파랑색 출력

color = raw_input("가장 좋아하는 색은?")
# =>빨간색 입력
print(color)
# =>빨간색 출력
