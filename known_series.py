"""Known Series.

This module contains known Taylor series of functions.
"""

from fractions import Fraction
from itertools import count

def _fact(n):
	res = 1
	for i in range(1, n+1):
		res *= i
	return res

def _binomial(n, k):
	return Fraction(_fact(n), _fact(k)*_fact(n-k))

# https://www.bernoulli.org
def _bernoulli(n):
	res = 0
	for k in range(n+1):
		fst_factor = Fraction(1, k+1)
		snd_factor = Fraction(0)
		for v in range(k+1):
			snd_factor += (-1)**v * _binomial(k, v) * v**n
		res += fst_factor*snd_factor
	return res

def sin():
	n = 0
	for i in count():
		if i%2 != 0:
			yield Fraction((-1)**n, _fact(2*n+1))
			n += 1
		else:
			yield 0

def cos():
	n = 0
	for i in count():
		if i%2 == 0:
			yield Fraction((-1)**n, _fact(2*n))
			n += 1
		else:
			yield 0

def tan():
	n = 1
	for i in count():
		if i%2 != 0:
			yield Fraction(_bernoulli(2*n) * (-4)**n * (1-4**n), _fact(2*n))
			n += 1
		else:
			yield 0

# FIXME
def cot():
	yield 1
	n = 1
	for i in count():
		if i%2 != 0:
			yield -Fraction(2**(2*n)*_bernoulli(n), _fact(2*n))
			n += 1
		else:
			yield 0

if __name__ == '__main__':
	c = cot()

	for i in range(10):
		print(next(c))
