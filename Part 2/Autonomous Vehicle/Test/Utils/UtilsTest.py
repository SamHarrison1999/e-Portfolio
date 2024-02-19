import unittest

from Main.Utils.Utils import is_null_or_white_space


class MyTestCase(unittest.TestCase):

    def testEmptyString(self):
        self.assertEqual(is_null_or_white_space(""), True)  # add assertion here

    def testNullString(self):
        self.assertEqual(is_null_or_white_space(None), True)  # add assertion here

    def testString(self):
        self.assertEqual(is_null_or_white_space("test string"), False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
