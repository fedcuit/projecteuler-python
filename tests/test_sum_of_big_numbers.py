from unittest import TestCase
from problems import problem13

__author__ = 'edfeng'


class TestProblem13(TestCase):
    def test_sum_of_big_numbers(self):
        self.assertEqual('5537376230', str(problem13.sum_of_big_numbers())[:10])