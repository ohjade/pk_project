# Just a simple test to test that testing works...
# Also template for adding new test functions in unittest format
# Run in Terminal with `python -m unittest <path/to/test.py>`

import unittest


def add(a, b):
    return a + b


class TestAdd(unittest.TestCase):
    def test_add(self):
        result = add(2, 3)
        self.assertEqual(result, 5)


if __name__ == "__main__":
    TestAdd()
    print("Test passed")
