# https://github.com/mrkobayashi25/lab10-mrkd-is
# Partner 1: Mason Downs
# Partner 2: Isabelle Sundin

import unittest
import math
from calculator import *



















class TestCalculator(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)

    def test_divide(self):
        self.assertEqual(divide(2, 10), 5)
        with self.assertRaises(ZeroDivisionError):
            divide(0, 5)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(1, 10)       # invalid base
        with self.assertRaises(ValueError):
            logarithm(-2, 10)      # negative base
        with self.assertRaises(ValueError):
            logarithm(2, -10)      # negative value

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(9), 3.0)
        with self.assertRaises(ValueError):
            square_root(-4)

#Partner 2's test functions

    def test_add():
        assert add(2, 3) == 5
        assert add(-1, -1) == -2
        assert add(0, 0) = 0
        print("test_add passed")

    def test_substract():
        assert sub(5, 2) == 3
        assert sub(0, 3) == -3
        assert sub(-2, -2) = 0
        print("test_sub passed")

    def test_divide_by_zero():
        try:
            div(0, 5)
        except ZeroDivisionError as e:
            print("test_divide_by_zero passed.")
        else:
            print("test_divide_by_zero failed.")

    def test_logarithm():
        assert round(log(10, 100), 6) == 2
        assert round(log(2, 8), 6) == 3
        print("test_logarithm passed.")

    def test_log_invalid_base():
        try:
            log(1, 10)
        except ValueError:
            print("test_log_invalid_base passed.")
        elseL
            print("test_log_invalid_base failed.")
        
