from itertools import islice
from fractions import Fraction

from sneaking_at_power_series import *
from known_series import *

Fraction.__repr__ = lambda self: "0" if self.numerator == 0 else \
                                 f"{self.numerator}" if self.denominator == 1 else \
                                 f"{self.numerator}/{self.denominator}"

def take(n, it):
	return tuple(islice(it, n))

print(list(islice(div(sin(), cos()), 10)))
s = sin()
_ = next(s) # should skip until a non zero is found
# [1, 0, -1/3, 0, -1/45, 0, -2/945, 0, -1/4725, 0]
print(list(islice(div(cos(), s), 10)))
print(take(10, cot()))
