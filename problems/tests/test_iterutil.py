from unittest import TestCase

from problems import iterutil


__author__ = 'edfeng'


class TestIterUtil(TestCase):
    def test_partition(self):
        self.assertEqual([[1, 2, 3], [4, 5, 6], [7, 8]], iterutil.partition([1, 2, 3, 4, 5, 6, 7, 8], 3))
        self.assertEqual([[1, 2, 3], [4, 5, 6], [7, 8, 9]], iterutil.partition([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))