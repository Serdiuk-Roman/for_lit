from unittest import TestCase, main
from dz import StringCalculator


class TestStringCalculator(TestCase):

    def setUp(self):
        self.test_obj = StringCalculator()

    def test_add(self):
        self.assertEqual(
            self.test_obj.add("5 3 2"),
            10
        )

    def test_add_empty_line(self):
        self.assertEqual(
            self.test_obj.add(""),
            0
        )

    def test_add_singular(self):
        self.assertEqual(
            self.test_obj.add("1"),
            1
        )

    def test_add_two_numbers_comma_separated(self):
        self.assertEqual(
            self.test_obj.add("10,20"),
            30
        )

    def test_add_two_numbers_newline_separated(self):
        self.assertEqual(
            self.test_obj.add("1\n2"),
            3
        )

    def test_add_numbers_sep_c_and_nl(self):
        self.assertEqual(
            self.test_obj.add("1\n2,3\n4"),
            10
        )

    def test_add_negative_numbers(self):
        self.assertEqual(
            self.test_obj.add("-1,2,-3"),
            'отрицательные числа запрещены: -1,-3'
        )

    def test_add_more_than_1000(self):
        self.assertEqual(
            self.test_obj.add("1000,2,3000"),
            2
        )

    def test_single_diviator(self):
        self.assertEqual(
            self.test_obj.add("//#\n1#2"),
            3
        )

    def test_multiple_diviator(self):
        self.assertEqual(
            self.test_obj.add("//###\n1###2"),
            3
        )


if __name__ == '__main__':
    main()
