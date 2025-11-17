# x = 5
# y = 4.5
# z = False
# print(type(x))
# print(type(y))
# print(type(z))
import math


# print(dir(x))

import math

class Fraction:
    def __init__(self, num, denom):
        self.numerator = num
        self.denominator = denom

    # def add(self, f):
    #     denom = math.lcm(self.numerator, self.denominator)
    #     num = (denom//self.denominator) * self.numerator +  (denom // f.denominator) * f.numerator
    #     return Fraction(num, denom)

    def __str__(self):
        return "{}/{}".format(self.numerator, self.denominator)

    def __add__(self, f):
        denom = math.lcm(self.numerator, self.denominator)
        num = (denom // self.denominator) * self.numerator + (denom // f.denominator) * f.numerator
        return Fraction(num, denom)

    def simplify(self):
        g = math.gcd(self.numerator, self.denominator)
        self.numerator = self.numerator // g
        self.denominator = self.denominator // g

f1 = Fraction(10, 40)
f2 = Fraction(20, 40)
# f3 = f1.add(f2)
f3 = f1 + f2
print(f3)
# print(f1)
#
# f1.simplify()
# print(f1)