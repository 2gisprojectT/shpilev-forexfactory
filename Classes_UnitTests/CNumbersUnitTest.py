__author__ = 'PunkBASSter'

from unittest import TestCase
from numbers import Numbers
import unittest


class NumbersTest(TestCase):
    def test_init(self):
        num = Numbers(1, 2, 3)
        self.assertEqual(1, num.a, 'A has wrong value')
        self.assertEqual(2, num.b, 'A has wrong value')
        self.assertEqual(3, num.c, 'A has wrong value')

    def test_sum_pos(self):
        num = Numbers(1, 2, 3)
        self.assertEqual(6, num.sum(), 'Sum with C>0 has wrong value')

    def test_sum_neg(self):
        num = Numbers(1, 2, -3)
        self.assertEqual(3, num.sum(), 'Sum with C<0 has wrong value')

    def test_mul_pos(self):
        num = Numbers(2, -2, 3)
        self.assertEqual(-12, num.multimlication(), 'Mul with C>0 has wrong value')

    def test_mul_neg(self):
        num = Numbers(2, 2, -3)
        self.assertEqual(0, num.multimlication(), 'Mul with C>0 has wrong value')

    def test_amul_pos(self):
        num = Numbers(2, -2, 3)
        self.assertEqual(12, num.abs_multimlication(), 'Mul with C>0 has wrong value')

    def test_amul_neg(self):
        num = Numbers(2, -2, -3)
        self.assertEqual(0, num.abs_multimlication(), 'Mul with C>0 has wrong value')

if __name__ == '__main__':
    unittest.main()