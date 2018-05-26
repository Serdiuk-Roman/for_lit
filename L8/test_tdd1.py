from unittest import TestCase, mock, main
from tdd1 import Greeter


class TestStringMethods(TestCase):

    def setUp(self):
        self.test_obj = Greeter()

    @mock.patch("tdd1.datetime")
    def test_greet_name(self, mock_time):
        mock_time.strftime.return_value = '15'
        self.assertEqual(
            self.test_obj.greet("Alf"),
            'Привет Alf'
        )

    @mock.patch("tdd1.datetime")
    def test_greet_cut_space(self, mock_time):
        mock_time.strftime.return_value = '15'
        self.assertEqual(
            self.test_obj.greet("   Alf   "),
            'Привет Alf'
        )

    @mock.patch("tdd1.datetime")
    def test_greet_capitalize(self, mock_time):
        mock_time.strftime.return_value = '15'
        self.assertEqual(
            self.test_obj.greet("alf"),
            'Привет Alf'
        )

    @mock.patch("tdd1.datetime")
    def test_greet_good_morning(self, mock_time):
        mock_time.strftime.return_value = '9'
        self.assertEqual(
            self.test_obj.greet("alf"),
            'Доброе утро Alf'
        )

    @mock.patch("tdd1.datetime")
    def test_greet_good_evening(self, mock_time):
        mock_time.strftime.return_value = '20'
        self.assertEqual(
            self.test_obj.greet("alf"),
            'Добрый вечер Alf'
        )

    @mock.patch("tdd1.datetime")
    def test_greet_good_night(self, mock_time):
        mock_time.strftime.return_value = '3'
        self.assertEqual(
            self.test_obj.greet("alf"),
            'Доброй ночи Alf'
        )

    # зделать тест с логированием


if __name__ == '__main__':
    main()
