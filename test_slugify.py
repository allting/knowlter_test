import unittest

from slugify import slugify


class SlugifyTest(unittest.TestCase):
    def test_lowercases_and_collapses_non_alphanumeric_characters(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")
        self.assertEqual(slugify("  Multiple---separators  "), "multiple-separators")

    def test_rejects_empty_or_non_alphanumeric_input(self):
        with self.assertRaises(ValueError):
            slugify("")
        with self.assertRaises(ValueError):
            slugify("--- !!! ---")


if __name__ == "__main__":
    unittest.main()
