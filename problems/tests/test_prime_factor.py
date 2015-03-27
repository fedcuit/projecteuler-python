from unittest import TestCase
from problems import problem3
__author__ = 'edfeng'


class TestProblem3(TestCase):
    def test_max_prime_factor(self):
        self.assertEqual(6857, max(problem3.prime_factors(600851475143)))