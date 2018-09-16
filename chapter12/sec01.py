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
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year

    honk = "빵빵"

    def info(self, color, year):
        print("color : %s, year:%d" % (color, year))


car1 = Car("Toyota", "red", 1996)
car2 = Car("Hyundi", "blue", 2006)
car3 = Car("BMW", "black", 2000)

