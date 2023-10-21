import unittest
from pkmodel.model import Model 


class TestModel(unittest.TestCase):

    def test_dose_function(self):
        test_model = Model("test_model", 2, "intravenous", 1, 1, 1, 1, 100, 1)
        result = test_model.dose(0, 100)
        self.assertEqual(result, 100)

if __name__ == '__main__':
    unittest.main()
