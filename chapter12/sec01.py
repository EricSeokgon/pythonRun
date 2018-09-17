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

    def __init__(self, color, year):
        self.color = color
        self.year = year
        print("새로운 Car 인스턴스가 생성되었습니다.")

    def get_info(self):
        print("color : %s, year : %d" % (self.color, self.year))


my_car = Car("red", 2017)
my_car.get_info()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("나는 부모 클래스 입니다.")


class Employee(Person):
    def info(self):
        print("나는 자식 클래스 입니다.")


per = Person("Python", 100)
per.info()

em = Employee("goorm", 20)
em.info()
