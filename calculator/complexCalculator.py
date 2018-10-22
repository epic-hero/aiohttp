from math import *
from .complex import Complex

class ComplexCalculator:
    def add(self, a, b):
        re = a.re + b.re
        im = a.im + b.im
        return Complex(re, im)

    def sub(self, a, b):
        re = a.re - b.re
        im = a.im - b.im
        return Complex(re, im)

    def mult(self, a, b):
        re = a.re * b.re - a.im * b.im
        im = a.re * b.im - a.im * b.re
        return Complex(re, im)

    def div(self, a, b):
        c = a.im * a.im + b.im * b.im
        re = (a.re * a.im + b.re * b.im) / c
        im = (b.re * a.im - a.re * b.im) / c
        return Complex(re, im)

    def mod(self, a):
        return sqrt(a.re * a.re + a.im * a.im)