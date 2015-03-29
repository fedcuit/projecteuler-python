from unittest import TestCase

from problems import problem25


__author__ = 'edfeng'


class TestProblem25(TestCase):
    def test_nth_fibonacci_with_specific_digits(self):
        self.assertEqual(4781, problem25.nth_fibonacci_with_specific_digits(1000))