from unittest import TestCase, mock, main
from hash import hash_md5


class MD5TestCase(TestCase):
    @mock.patch('hash.md5')
    def test_some_test(self, mock_md5):
        hash_md5('Some Str')
        mock_md5.assert_called_with("Some Str".encode())


if __name__ == "__main__":
    main()
