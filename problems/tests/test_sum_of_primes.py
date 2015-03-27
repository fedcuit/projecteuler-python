from unittest import TestCase
from problems import problem10

__author__ = 'edfeng'


class TestProblem10(TestCase):
    def test_sum_of_primes(self):
        self.assertEqual(17, problem10.sum_of_primes(10))
        self.assertEqual(142913828922, problem10.sum_of_primes(2000000))