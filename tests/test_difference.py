from unittest import TestCase
from problems import problem6

__author__ = 'edfeng'


class TestProblem6(TestCase):
    def test_difference(self):
        self.assertEqual(2640, problem6.difference(xrange(1, 11)))
        self.assertEqual(25164150, problem6.difference(xrange(1, 101)))