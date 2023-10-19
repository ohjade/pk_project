import unittest
import pkmodel as pk
import numpy as np
import scipy.integrate
from pkmodel.model import Model 
import unittest

#I know there should be a way to just import these functions directly for each test but I keep having problems with importing! So I'm just gonna re-define the functions here for now (not good practice, I know :( )

# functions:
def dose(t,X):
    return X

def rhs(t, y, Q_p1, V_c, V_p1, CL, X):
    q_c, q_p1 = y
    transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)
    dqc_dt = dose(t, X) - q_c / V_c * CL - transition
    dqp1_dt = transition
    return [dqc_dt, dqp1_dt]

t_eval = np.linspace(0, 1, 1000)
y0 = np.array([0.0, 0.0])

class TestRHS(unittest.TestCase):
    def test_rhs(self):
        t = 1
        y = [1,1]
        Q_p1 = 1
        V_c = 1
        V_p1 = 1
        CL = 1
        X = 1

        result = rhs(t, y, Q_p1, V_c, V_p1, CL, X)

        # Define expected results
        expected_dqc_dt = (X - y[0] / V_c * CL - Q_p1 * ((y[0] / V_c) - (y[1] / V_p1)))
        expected_dqp1_dt = Q_p1 * ((y[0] / V_c - y[1] / V_p1))

        # Check if results match expected values
        self.assertEqual(result[0], expected_dqc_dt) # Tests rate of change in central compartment
        self.assertEqual(result[1], expected_dqp1_dt) # Tests rate of change in peripheral compartment

    def test_rhs_negative(self):
        t = 1
        y = [1,1]
        Q_p1 = -1
        V_c = 1
        V_p1 = 1
        CL = -1 
        X = 1

        result = rhs(t, y, Q_p1, V_c, V_p1, CL, X)

        # Define expected results
        expected_dqc_dt = (X - y[0] / V_c * CL - Q_p1 * ((y[0] / V_c) - (y[1] / V_p1)))
        expected_dqp1_dt = Q_p1 * ((y[0] / V_c - y[1] / V_p1))

        # Check if results match expected values
        self.assertEqual(result[0], expected_dqc_dt) # Tests rate of change in central compartment
        self.assertEqual(result[1], expected_dqp1_dt) # Tests rate of change in peripheral compartment

    def test_rhs_dividebyzero(self):
        "Raise Error if tries to divide by zero"
        t = 1
        y = [1,1]
        Q_p1 = 1
        V_c = 0
        V_p1 = 1
        CL = 1
        X = 1

        result = rhs(t, y, Q_p1, V_c, V_p1, CL, X)
        # Define expected results
        expected_dqc_dt = (X - y[0] / V_c * CL - Q_p1 * ((y[0] / V_c) - (y[1] / V_p1)))
        expected_dqp1_dt = Q_p1 * ((y[0] / V_c - y[1] / V_p1))

        # Raise error if the denominator values are zero
        



class TestODE(unittest.TestCase):
    #Still working on this one
    def test_sol(self): 
        model = {
            'name': 'model1',
            'Q_p1': 1.0,
            'V_c': 1.0,
            'V_p1': 1.0,
            'CL': 1.0,
            'X': 1.0}
        
        args = [
        model['Q_p1'], model['V_c'], model['V_p1'], model['CL'], model['X']
    ]
        sol = scipy.integrate.solve_ivp(
            fun=lambda t, y: rhs(t, y, *args),
            t_span=[t_eval[0], t_eval[-1]],
            y0=y0, t_eval=t_eval
        )

#This bit prints the test result in the terminal
if __name__ == '__main__':
    unittest.main()