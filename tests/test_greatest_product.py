from unittest import TestCase
from problems import problem8

__author__ = 'edfeng'


class TestProblem8(TestCase):
    def test_greatest_produce(self):
        self.assertEqual(5832, problem8.greatest_product(4))
        self.assertEqual(23514624000, problem8.greatest_product(13))