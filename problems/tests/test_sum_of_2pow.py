from unittest import TestCase
from problems import problem16

__author__ = 'edfeng'


class TestProblem16(TestCase):
    def test_sum_of_2pow(self):
        self.assertEqual(26, problem16.sum_of_2pow(15))
        self.assertEqual(1366, problem16.sum_of_2pow(1000))