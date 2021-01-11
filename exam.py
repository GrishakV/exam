#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


#   Создать класс Triad (тройка чисел); определить методы изменения полей и вычисления
#   суммы чисел. Определить производный класс Triangle с полями-сторонами. Определить
#   методы вычисления углов и площади треугольника.

class Triad:

    def __init__(self, first=1, second=1, third=1):
        self.first = float(first)
        self.second = float(second)
        self.third = float(third)

    def read(self):
        first = input('Введите первое число: ')
        second = input('Введите второе число: ')
        third = input('Введите третье число: ')

        self.first = float(first)
        self.second = float(second)
        self.third = float(third)

    def sum(self):
        return self.first + self.second + self.third


class Triangle(Triad):
    def __init__(self, first=1, second=1, third=1):
        super(Triangle, self).__init__(first, second, third)

        self.corner()

    def per(self):
        return self.first + self.second + self.third

    def square(self):
        p = self.per() / 2
        return f"Площадь = {math.sqrt(p * (p - self.first) * (p - self.second) * (p - self.third))}"

    def corner(self):
        a = self.first
        b = self.second
        c = self.third

        first_corner = math.acos(((b ** 2) + (c ** 2) - (a ** 2)) / (2 * c * b))
        self.f_d = math.degrees(first_corner)

        second_corner = math.acos(((a ** 2) + (b ** 2) - (c ** 2)) / (2 * a * b))
        self.s_d = math.degrees(second_corner)

        third_corner = math.acos(((a ** 2) + (c ** 2) - (b ** 2)) / (2 * a * c))
        self.th_d = math.degrees(third_corner)

        return f"Первый угол = {self.f_d}°, Второй угол = {self.s_d}°, Третий угол = {self.th_d}°."


if __name__ == '__main__':
    r1 = Triad()
    r1.read()
    print(r1.sum())

    r2 = Triangle()
    r2.read()
    print(r2.square())
    print(r2.corner())
