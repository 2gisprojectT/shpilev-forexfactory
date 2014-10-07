__author__ = 'PunkBASSter'

import math
class Numbers:
    def __init__(self, a, b, c):
        self.a=a
        self.b=b
        if c > 0:
            self.c = c
        else:
            self.c = 0

    def sum(self):
        return self.a + self.b + self.c

    def multimlication(self):
        return self.a * self.b * self.c

    def abs_multiplication(self):
        return math.fabs(self.a * self.b * self.c)


num = Numbers(3,10,-2)

print(num.sum())
print(num.multimlication())
print(num.abs_multiplication())
