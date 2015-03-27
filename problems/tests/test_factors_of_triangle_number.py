from unittest import TestCase
from problems import problem12

__author__ = 'edfeng'


class TestProblem12(TestCase):
    def test_factors_of_triangle_number(self):
        self.assertEqual(28, problem12.factors_of_triangle_number(5))
        self.assertEqual(76576500, problem12.factors_of_triangle_number(500))