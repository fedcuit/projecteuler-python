from unittest import TestCase

from problems import problem1


__author__ = 'edfeng'


class TestProblem1(TestCase):
    def test_sum_of_multiples_of_3_or_5_under_1000(self):
        self.assertEqual(233168, problem1.sum_of_multiples(1000))