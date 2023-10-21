import unittest
import pkmodel as pk
from pkmodel.model import Model
from pkmodel.protocol import Protocol

class ProtocolTest(unittest.TestCase):
    """
    Tests the :class:`Protocol` class.
    """

    def test_evaluate(self):
        test_model = Model("test_model", 2, "intravenous", 1, 1, 1, 1, 1, 1)
        input_dict = (test_model.__dict__)
        test_evaluate = Protocol.evaluate()
        expected_test_evaluate = (input_dict['method'])
        self.assertEqual(test_evaluate, expected_test_evaluate)
        
    if __name__ == '__main__':
        unittest.main()

