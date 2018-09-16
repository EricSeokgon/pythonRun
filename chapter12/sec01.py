# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# 자동차1
car_brand1 = "Toyota"
car_color1 = "red"
car_year1 = 1996

car_brand2 = "Hyendi"
car_color2 = "blue"
car_year2 = 2009

car_brand3 = "BMW"
car_color3 = "black"
car_year3 = 2000


class Car:
    honk = "빵빵"

    def set_info(self, color, year):
        self.color = color
        self.year = year

    def get_info(self):
        print("color : %s, year : %d" % (self.color, self.year))


my_car = Car()
my_car.set_info("red", 2017)
my_car.get_info()
