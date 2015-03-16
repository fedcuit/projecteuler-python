from unittest import TestCase
from problems import problem22

__author__ = 'edfeng'


class TestProblem22(TestCase):
    def test_alpha_value(self):
        self.assertEqual(53, problem22.alpha_value('COLIN'))