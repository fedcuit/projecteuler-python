from unittest import TestCase
from problems import problem9

__author__ = 'edfeng'


class TestProblem9(TestCase):
    def test_pythagorean_triplet(self):
        self.assertEqual(31875000, problem9.the_triplet())