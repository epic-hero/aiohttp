from .complex import Complex
from .complexCalculator import ComplexCalculator

class ComplexVectorCalculator(ComplexCalculator):
    def add(self, a, b):
        c = []
        for i in range(len(a)):
            c.append(super(ComplexVectorCalculator, self).add(a[i], b[i]))
        return c

    def sub(self, a, b):
        c = []
        for i in range(len(a)):
            c.append(super(ComplexVectorCalculator, self).sub(a[i], b[i]))
        return c

    def mult(self, a, b):
        c = []
        for i in range(len(a)):
            c.append(super(ComplexVectorCalculator, self).mult(a[i], b[i]))
        return c

    def div(self, a, b):
        c = []
        for i in range(len(a)):
            c.append(super(ComplexVectorCalculator, self).div(a[i], b[i]))
        return c

    def mod(self, a):
        c = []
        for i in range(len(a)):
            c.append(super(ComplexVectorCalculator, self).mod(a[i]))
        return c