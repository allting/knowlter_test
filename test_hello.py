import unittest

from hello import greet


class GreetTest(unittest.TestCase):
    def test_greet_name(self):
        self.assertEqual(greet("세계"), "안녕, 세계!")

    def test_greet_empty_name(self):
        with self.assertRaises(ValueError):
            greet("")


if __name__ == "__main__":
    unittest.main()
