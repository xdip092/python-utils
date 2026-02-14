import unittest

from py_utils import chunk_list, moving_average, normalize_text


class TestPyUtils(unittest.TestCase):
    def test_normalize_text(self):
        self.assertEqual(normalize_text("  Hello   World  "), "hello world")

    def test_chunk_list(self):
        self.assertEqual(chunk_list([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]])

    def test_moving_average(self):
        self.assertEqual(moving_average([10, 20, 30, 40], window=2), [15, 25, 35])


if __name__ == "__main__":
    unittest.main()
