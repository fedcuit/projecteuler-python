from unittest import TestCase

from problems import problem17


__author__ = 'edfeng'


class TestProblem17(TestCase):
    def test_read_single_number(self):
        self.assertEqual("one,two,three,four,five,six,seven,eight,nine".split(","),
                         [problem17.read_number(i) for i in range(1, 10)])

    def test_read_teen_number(self):
        self.assertEqual("eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen".split(","),
                         [problem17.read_number(i) for i in range(11, 20)])

    def test_read_ty_number(self):
        self.assertEqual("twenty,thirty,forty,fifty,sixty,seventy,eighty,ninety".split(","),
                         [problem17.read_number(i) for i in range(20, 100, 10)])

    def test_read_ty_plus_single_number(self):
        numbers = """
            twenty-one,twenty-two,twenty-three,twenty-four,twenty-five,
            twenty-six,twenty-seven,twenty-eight, twenty-nine
            """
        import re
        self.assertEqual(
            re.sub(r'[\r\n\s+]', '', numbers).split(','),
            [problem17.read_number(i) for i in range(21, 30)])

    def test_read_hundreds(self):
        self.assertEqual("three hundred and forty-two", problem17.read_number(342))
        self.assertEqual("one hundred and fifteen", problem17.read_number(115))
        self.assertEqual("one hundred and five", problem17.read_number(105))
        self.assertEqual("one hundred", problem17.read_number(100))
        self.assertEqual("nine hundred and ninety-nine", problem17.read_number(999))

    def test_read_thousand(self):
        self.assertEqual("one thousand", problem17.read_number(1000))

    def test_number_of_letters(self):
        self.assertEqual(23, problem17.number_of_letters("three hundred and forty-two"))

    def test_number_of_letters_in_a_sequence(self):
        self.assertEqual(21124, problem17.result())