import unittest
from utils import utils

class TestUtils(unittest.TestCase):

    # Tests for reversed()
    def test_reversed_integer(self):
        self.assertEqual(utils.reversed(123), 321)

    def test_reversed_string(self):
        with self.assertRaises(TypeError):
            utils.reversed("123")

    def test_reversed_float(self):
        with self.assertRaises(TypeError):
            utils.reversed(123.4)

    # Tests for formatter()
    def test_formatter_integer(self):
        self.assertEqual(utils.formatter(8), (bin(8), oct(8)))

    def test_formatter_string(self):
        with self.assertRaises(TypeError):
            utils.formatter("8")

    def test_formatter_float(self):
        with self.assertRaises(TypeError):
            utils.formatter(8.5)

if __name__ == "__main__":
    unittest.main()