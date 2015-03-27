from unittest import TestCase

from problems import problem20


__author__ = 'edfeng'


class TestProblem20(TestCase):
    def test_sum_of_digits_in_factorial(self):
        self.assertEqual(27, problem20.sum_of_digits_in_factorial(10))
        self.assertEqual(648, problem20.sum_of_digits_in_factorial(100))