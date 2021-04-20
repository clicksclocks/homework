import unittest
import solver

class TestSolver(unittest.TestCase):
	def test_two_roots(self):
		self.assertEqual((2,3.0,-2.0), solver.solve(1,-1,-6))
	def test_one_root(self):
		self.assertEqual((1,-1.0), solver.solve(1,2,1))
	def test_zero_roots(self):
		self.assertEqual(('No roots'), solver.solve(0,0,1))
	def test_alone_root(self):
		self.assertEqual((1, -1.0),solver.solve(0,1,1))
	def test_complex_roots(self):
		self.assertEqual(('No real roots'),solver.solve(1,1,1))
	def test_infinite_roots(self):
		self.assertEqual(('Infinite roots'),solver.solve(0,0,0))

if __name__=="__main__":
	unittest.main()