# https://github.com/mrkobayashi25/lab10-mrkd-is
# Partner 1: Mason Downs
# Partner 2: Isabelle Sundin

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    # Partner 1 Tests
    def test_multiply(self):
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)

    def test_divide(self):
        self.assertEqual(div(2, 10), 5)
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(1, 10)
        with self.assertRaises(ValueError):
            logarithm(-2, 10)
        with self.assertRaises(ValueError):
            logarithm(2, -10)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(9), 3.0)
        with self.assertRaises(ValueError):
            square_root(-4)

    # Partner 2 Tests
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(0, 0), 0)

    def test_sub(self):
        self.assertEqual(sub(5, 3), 2)
        self.assertEqual(sub(0, 3), -3)
        self.assertEqual(sub(-2, -2), 0)

    def test_exp(self):
        self.assertEqual(exp(2, 3), 8)
        self.assertEqual(exp(10, 0), 1)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(10, 100), 2.0)
        self.assertAlmostEqual(logarithm(2, 8), 3.0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1, 10)
        with self.assertRaises(ValueError):
            logarithm(-2, 10)
        with self.assertRaises(ValueError):
            logarithm(10, -2)
