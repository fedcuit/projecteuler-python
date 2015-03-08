from unittest import TestCase
from problems import problem4

__author__ = 'edfeng'


class TestProblem4(TestCase):
    def test_is_palindrome(self):
        self.assertTrue(problem4.is_palindromic(9009))
        self.assertTrue(problem4.is_palindromic(90109))

    def test_max_palindrome(self):
        self.assertTrue(9009, problem4.palindromes(xrange(10, 100), xrange(10, 100)))
        self.assertTrue(906609, problem4.palindromes(xrange(100, 1000), xrange(100, 1000)))