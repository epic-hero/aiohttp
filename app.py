from aiohttp import web
import os
from application.router.Router import Router

app = web.Application()

Router(app, web)

web.run_app(app)

# from db.ORM import ORM

# orm = ORM('test.db')

# print(orm.getValue('user'))

# print('CgeJI9JIb')


# сделать выбор сепараторов and, or

# from calculator.complex import Complex
# #from calculator.complexCalculator import ComplexCalculator
# #from calculator.complexVectorCalculator import ComplexVectorCalculator
# from calculator.complexVectorMatrixCalculator import ComplexVectorMatrixCalculator

# calc = ComplexVectorMatrixCalculator()

# a = [
#     [Complex(2, 3), Complex(3, 5), Complex(4, 10)],
#     [Complex(2, 3), Complex(3, 5), Complex(4, 10)],
#     [Complex(2, 3), Complex(3, 5), Complex(4, 10)]
# ]
# b = [
#     [Complex(5, 11), Complex(6, 12), Complex(7, 13)],
#     [Complex(5, 11), Complex(6, 12), Complex(7, 13)],
#     [Complex(5, 11), Complex(6, 12), Complex(7, 13)],
# ]
# #a = Complex(2, 3)
# #b = Complex(5, 11)
# c = calc.div(a, b)

# print(c)

# #print(str(c.re) + ', ' + str(c.im))
