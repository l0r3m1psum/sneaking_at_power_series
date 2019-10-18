"""Sneaking at Power Series.

This module is a Python version of Squinting at Power Series, it is also
inspired by Power Serius another work of M. Douglas Mcllroy.

Sources:
https://swtch.com/~rsc/thread/squint.pdf
https://www.cs.dartmouth.edu/~doug/music.ps.gz
https://www.cs.dartmouth.edu/~doug/pearl.ps.gz
https://www.cs.dartmouth.edu/~doug/powser.html
Knuth Vol. 2"""

from itertools import tee

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


# Q = F/G = f/g + (F' - (f/g)G')/G
# the firs coefficent of G must be zero!
def div(F, G):
	"""Divides two power series."""
	G, G1 = tee(G)
	q = next(F) / next(G)
	yield q
	yield from div(sub(F, mulc(q, G)), G1)

def deriv(F):
	"""Derivate a power serie."""
	_ = next(F)
	for n, a in enumerate(F, 1):
		yield n * a

# TODO: add Fraction
def integr(F, const):
	"""Integrate a power serie."""
	yield const
	for n, a in enumerate(F, 1):
		yield 1/n * a

# F(G) = f + g*F' + G'*F'(G)
# this assumes g to be 0
# F(G) = f + G'*F'(G)
def comp(F, G):
	"""Composes two power series."""
	G, G1 = tee(G)
	yield next(F)
	_ = next(G)
	yield from mul(G, comp(F, G1))

# TODO:
def recip(F):
	"""Reciprocal of a power serie."""
	pass

