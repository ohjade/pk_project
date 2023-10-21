import unittest
from pkmodel.model import Model
from pkmodel.solution import Solver
import numpy as np
import scipy

class TestSolution(unittest.TestCase):
    """
    Tests the :class:`Solution` class.
    """
    
    def setUp(self):
        #Arguments for model testing
        self.model = Model("test_model", 2, "intravenous", 1, 1, 1, 1, 1, 1)
        self.Solver = Solver(self.model)
        
    # def test_solve_ivp(self):
    #     result = self.Solver.solve_ivp()
    #     expected_result = 
        
if __name__ == '__main__':
    unittest.main()
