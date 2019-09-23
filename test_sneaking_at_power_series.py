import unittest
from sneaking_at_power_series import *
from itertools import islice, count, repeat

class Tests(unittest.TestCase):

	def test_add(self):
		# elem. neutro
		self.assertEqual(list(islice(add(count(), repeat(0)), 10)),
		                 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
		self.assertEqual(list(islice(add(repeat(0), count(0)), 10)),
		                 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

		self.assertEqual(list(islice(add(count(), count()), 10)),
		                 [0, 2, 4, 6, 8, 10, 12, 14, 16, 18])

	def test_neg(self):
		# elem. neutro
		self.assertEqual(list(islice(neg(repeat(0)), 10)),
		                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

		self.assertEqual(list(islice(neg(count(0)), 10)),
		                 [0, -1, -2, -3, -4, -5, -6, -7, -8, -9])

	def test_sub(self):
		# elem. neutro
		self.assertEqual(list(islice(sub(count(), repeat(0)), 10)),
		                 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

		self.assertEqual(list(islice(sub(repeat(0), count()), 10)),
		                 [0, -1, -2, -3, -4, -5, -6, -7, -8, -9])
		# elem. annullatore
		self.assertEqual(list(islice(sub(count(0), count(0)), 10)),
		                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

	def test_mul(self):
		# elem. annullatore
		self.assertEqual(list(islice(mul(count(), repeat(0)), 10)),
		                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

		self.assertEqual(list(islice(mul(count(1), count(1)), 10)),
		                 [1, 4, 10, 20, 35, 56, 84, 120, 165, 220])

	def test_mulc(self):
		# elem. annnullatore
		self.assertEqual(list(islice(mulc(0, count()), 10)),
		                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
		# elem neutro
		self.assertEqual(list(islice(mulc(1, count()), 10)),
		                 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

		self.assertEqual(list(islice(mulc(-1, count()), 10)),
		                 [0, -1, -2, -3, -4, -5, -6, -7, -8, -9])


	def test_div(self):
		self.assertEqual(list(islice(div(count(1), count(1)), 10)),
		                 [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

	def test_deriv(self):
		self.assertEqual(list(islice(deriv(count(0)), 10)),
		                 [1, 4, 9, 16, 25, 36, 49, 64, 81, 100])
		self.assertEqual(list(islice(integr(deriv(count(1)), 1), 10)),
		                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

	def test_integr(self):
		self.assertEqual(list(islice(integr(count(1), 0), 10)),
		                 [0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
		self.assertEqual(list(islice(deriv(integr(count(1), 0)), 10)),
		                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

	def test_euristics(self):
		"""I don't know if they are correct and they should be removed."""
		self.assertEqual(list(islice(mul(count(), repeat(1)), 10)), 
		                 [0, 1, 3, 6, 10, 15, 21, 28, 36, 45])
		# is it correct?
		self.assertEqual(list(islice(comp(count(1), count(1)), 10)), 
		                 [1, 4, 18, 76, 309, 1224, 4756, 18208, 68892, 258176])
		 # seems legit
		self.assertEqual(list(islice(comp(repeat(1), repeat(1)), 10)), 
		                 [1, 1, 2, 4, 8, 16, 32, 64, 128, 256])

	def test_sin(self):
		self.assertEqual(list(islice(deriv(sin()), 10)),
		                 list(islice(cos(), 10)))

	# FIXME: assertAlmostEqual on all element of the list or use Fraction()
	# def test_cos(self):
	# 	self.assertEqual(list(islice(deriv(cos()), 10)),
	# 	                 list(islice(neg(sin()), 10)))

if __name__ == '__main__':
	unittest.main()
