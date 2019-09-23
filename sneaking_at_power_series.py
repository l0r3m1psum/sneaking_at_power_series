"""Sneaking at Power Series.

This module is a Python version of Squinting at Power Series, it is also
inspired by Power Serius another work of M. Douglas Mcllroy.

Sources:
https://swtch.com/~rsc/thread/squint.pdf
https://www.cs.dartmouth.edu/~doug/music.ps.gz
https://www.cs.dartmouth.edu/~doug/pearl.ps.gz
https://www.cs.dartmouth.edu/~doug/powser.html
Knuth Vol. 2"""

from itertools import  tee, count
from fractions import Fraction

# F+G = f+g + F'+G'
def add(F, G):
	"""Adds two power series."""
	yield next(F) + next(G)
	yield from add(F, G)

# -F = -f + -F'
def neg(F):
	"""Negate a power serie."""
	yield -next(F)
	yield from neg(F)

# F-G = F + -G
def sub(F, G):
	"""Subtracts two power series."""
	yield from add(F, neg(G))

def mulc(const, F):
	"""Multiply a power serie with a constant."""
	yield const*next(F)
	yield from mulc(const, F)

# F*G = f*g + f*F' + F'*G
def mul(F, G):
	"""Multiplies two power series."""
	G, G1 = tee(G)
	f = next(F)
	yield f * next(G)
	yield from add(mulc(f, G), mul(F, G1))


# Q = F/G = f/g + (1/g)*(F' - Q*G')
# this assumes that all coefficient of G are different from 0
def div(F, G):
	"""Divides two power series."""
	F, F1 = tee(F)
	G, G1 = tee(G)
	g = next(G)
	yield next(F) / g
	yield from mulc(1/g, sub(F, mul(div(F1, G1), G)))

def deriv(F):
	"""Derivate a power serie."""
	_ = next(F)
	for n, a in enumerate(F, 1):
		yield n * a

def integr(F, const):
	"""Integrate a power serie."""
	yield const
	for n, a in enumerate(F, 1):
		yield 1/n * a

# TODO:
# https://en.wikipedia.org/wiki/Binomial_theorem
def exp(F, const):
	"""Elevate a power serie to a given constant."""
	pass

# TODO:
# F(G) = f + G'*F'(G)
# F(G) = f + g*F' + G'*F'(G)
# this assumes g to be 0
def comp(F, G):
	"""Composes two power series."""
	G, G1 = tee(G)
	yield next(F)
	_ = next(G)
	yield from mul(G, comp(F, G1))
	# F(G) = f + F'(G)
	# yield next(F)
	# yield from comp(F, G)

# TODO:
def recip(F):
	"""Reciprocal of a power serie."""
	pass

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

if __name__ == '__main__':
	Fraction.__repr__ = lambda self: "0" if self.numerator == 0 else \
	                                 f"{self.numerator}" if self.denominator == 1 else \
	                                 f"{self.numerator}/{self.denominator}"
