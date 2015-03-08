from unittest import TestCase
from problems import problem5

__author__ = 'edfeng'


class TestProblem5(TestCase):
    def test_smallest_number(self):
        self.assertEqual(2520, problem5.smallest_number(range(1, 11)))