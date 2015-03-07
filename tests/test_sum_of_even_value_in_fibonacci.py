from unittest import TestCase
import itertools

from problems import problem2


__author__ = 'edfeng'


class TestProblem2(TestCase):
    def test_sum_of_even_value_in_fibonacci(self):
        self.assertEqual(4613732, problem2.sum_of_fibs())