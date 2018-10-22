from .complex import Complex
from .complexVectorCalculator import ComplexVectorCalculator

class ComplexVectorMatrixCalculator(ComplexVectorCalculator):
    def add(self, a, b):
        c = []
        for i in range(len(a)):
            c.append(super(ComplexVectorMatrixCalculator, self).add(a[i], b[i]))
        return c

    def sub(self, a, b):
        c = []
        for i in range(len(a)):
            c.append(super(ComplexVectorMatrixCalculator, self).sub(a[i], b[i]))
        return c

    def mult(self, a, b):
        c = []
        for i in range(len(a)):
            c.append(super(ComplexVectorMatrixCalculator, self).mult(a[i], b[i]))
        return c

    def div(self, a, b):
        c = []
        for i in range(len(a)):
            c.append(super(ComplexVectorMatrixCalculator, self).div(a[i], b[i]))
        return c

    def mod(self, a):
        c = []
        for i in range(len(a)):
            c.append(super(ComplexVectorMatrixCalculator, self).mod(a[i]))
        return c