# Just a simple test to test that testing works...
# Also template for adding new test functions in unittest format
# Run in Terminal with `python -m unittest <path/to/test.py>`

import unittest


def add(a, b, c):
    return a + b + c


class TestAdd(unittest.TestCase):
    def test_add(self):
        result = add(2, 3, 3)
        self.assertEqual(result, 8)


if __name__ == "__main__":
    TestAdd()
    print("Test passed")
