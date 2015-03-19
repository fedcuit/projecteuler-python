from unittest import TestCase
from problems import problem23

__author__ = 'edfeng'


class TestProblem23(TestCase):
    def test_is_abundant_number(self):
        self.assertTrue(problem23.is_abundant_number(12))

    def test_none_abundantify_numbers(self):
        self.assertEqual(4179871, sum(problem23.none_abundantify_numbers()))