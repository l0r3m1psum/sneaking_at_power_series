"""Sneaking at Power Series.

This module is a Python version of Squinting at Power Series, it is also
inspired by Power Serius another work of M. Douglas Mcllroy.

Sources:
https://swtch.com/~rsc/thread/squint.pdf
https://www.cs.dartmouth.edu/~doug/powser.html
https://en.wikipedia.org/wiki/Power_series"""

from itertools import  tee

# TODO: fare le prove con sin, cos, sinh, cosh, exp, ecc per la precisione dei numeri

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

if __name__ == '__main__':
	# from sys import getrecursionlimit, setrecursionlimit
	# print(getrecursionlimit()) # 1_000
	# setrecursionlimit(10_000)
	from itertools import islice, count, repeat
	# lol 14 is the max, after that you hit RecursionError
	print(list(islice(div(count(), repeat(2)), 14)))
	# print(list(islice(div(count(), repeat(2)), 25)))

