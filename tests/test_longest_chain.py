from unittest import TestCase
from problems import problem14

__author__ = 'edfeng'


class TestProblem14(TestCase):
    def test_staring_number_has_longest_chain(self):
        self.assertEqual(837799, problem14.longest_chain())