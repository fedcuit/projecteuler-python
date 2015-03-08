from unittest import TestCase
from problems import problem7

__author__ = 'edfeng'


class TestProblem7(TestCase):
    def test_nth_prime(self):
        self.assertEqual(13, problem7.nth_prime(6))
        self.assertEqual(104743, problem7.nth_prime(10001))