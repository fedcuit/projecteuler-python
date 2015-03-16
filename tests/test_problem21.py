from unittest import TestCase
import itertools

from problems import problem21


__author__ = 'edfeng'


class TestProblem21(TestCase):
    def test_sum_of_proper_divisor(self):
        self.assertEqual(284, problem21.sum_of_proper_divisor(220))
        self.assertEqual(220, problem21.sum_of_proper_divisor(284))

    def test_is_amicable_number(self):
        self.assertTrue(problem21.is_amicable_number(284))
        self.assertTrue(problem21.is_amicable_number(220))

    def test_sum_of_amicables(self):
        amicables_number_10000 = itertools.takewhile(lambda x: x < 10000, problem21.amicables())
        self.assertEqual(31626, sum(amicables_number_10000))