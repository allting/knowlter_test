import unittest

from total import total


class TotalTest(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(total([]), 0)

    def test_sums_integers(self):
        self.assertEqual(total([1, 2, 3, -4]), 2)

    def test_rejects_non_integer(self):
        with self.assertRaises(TypeError):
            total([1, "2", 3])


if __name__ == "__main__":
    unittest.main()
