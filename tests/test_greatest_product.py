from unittest import TestCase
from problems import problem8
from problems import problem11

__author__ = 'edfeng'


class TestProblem8(TestCase):
    def test_greatest_product(self):
        self.assertEqual(5832, problem8.greatest_product(4))
        self.assertEqual(23514624000, problem8.greatest_product(13))


class TestProblem11(TestCase):
    def test_greatest_product(self):
        self.assertEqual(70600674, problem11.greatest_product())