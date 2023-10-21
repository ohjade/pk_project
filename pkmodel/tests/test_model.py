import unittest
from pkmodel.model import Model


class TestModel(unittest.TestCase):

    def test_dose_function(self):
        test_model = Model("test_model", 1, "intravenous", 1, 1, 1, 1, 1, 1)
        result = test_model.dose(0, 10)
        self.assertEqual(result, 10)

    def test_solve_function(self):
        test_model = Model("test_model", 1, "intravenous", 1, 1, 1, 1, 1, 1)
        sol = test_model.solve()


if __name__ == "__main__":
    unittest.main()
