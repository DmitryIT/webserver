import unittest
from unittest import TestCase

from webserver.response import get_response


class Test(TestCase):
    def test_get_response(self):
        self.assertEqual(get_response(), b'Hello world!')


if __name__ == '__main__':
    unittest.main()