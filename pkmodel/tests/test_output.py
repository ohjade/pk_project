import unittest
import numpy as np
from pkmodel.model import Model
from pkmodel.solution import Solver


# This test aims to act as an equation template to check our model against. If errors appear in this test, it's possible that our rhs equation has been edited/mistyped.

# To do: parameterise tests to shorten code

# functions:
def dose(t, X):
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
        """Test that rhs function returns correct output based on model ODEs"""
        t = 1
        y = [1, 1]
        Q_p1 = 1
        V_c = 1
        V_p1 = 1
        CL = 1
        X = 1

        result = rhs(t, y, Q_p1, V_c, V_p1, CL, X)

        # Define expected results
        term2 = y[0] / V_c * CL
        term3 = Q_p1 * ((y[0] / V_c) - (y[1] / V_p1))
        expected_dqc_dt = X - term2 - term3
        calculated_dqc_dt = (
            0  # Value calculated manually to ensure no errors in rhs equation
        )
        expected_dqp1_dt = Q_p1 * ((y[0] / V_c - y[1] / V_p1))
        calculated_dqp1_dt = (
            100  # Value calculated manually to ensure no errors in rhs equation
        )

        # Check if results match expected values
        self.assertEqual(
            result[0], expected_dqc_dt, calculated_dqc_dt
        )  # Tests rate of change in central compartment
        self.assertEqual(
            result[1], expected_dqp1_dt, calculated_dqp1_dt
        )  # Tests rate of change in peripheral compartment

    def test_rhs_negative(self):
        """
        Test that rhs function returns correct output based on model ODEs,
        even if input values are negative
        """
        t = 1
        y = [1, 1]
        Q_p1 = -1
        V_c = 1
        V_p1 = 1
        CL = -1
        X = 1

        result = rhs(t, y, Q_p1, V_c, V_p1, CL, X)

        # Define expected results
        term2 = y[0] / V_c * CL
        term3 = Q_p1 * ((y[0] / V_c) - (y[1] / V_p1))
        expected_dqc_dt = X - term2 - term3
        # Value calculated manually to ensure no errors in rhs equation
        # (makes this test for negative unnecessary I guess)

        # Commented out for now as formatter didn't want unsed variables
        # calculated_dqc_dt = 2
        expected_dqp1_dt = Q_p1 * ((y[0] / V_c - y[1] / V_p1))
        # calculated_dqp1_dt = (
        #     0  # Value calculated manually to ensure no errors in rhs eq
        # )

        # Check if results match expected values
        self.assertEqual(
            result[0], expected_dqc_dt
        )  # Tests rate of change in central compartment
        self.assertEqual(
            result[1], expected_dqp1_dt
        )  # Tests rate of change in peripheral compartment

    # def test_rhs_dividebyzero(self):
    #     "Raise Error if tries to divide by zero"
    #     t = 1
    #     y = [1, 1]
    #     Q_p1 = 1
    #     V_c = 0
    #     V_p1 = 1
    #     CL = 1
    #     X = 1

    #     # Raise error if the denominator values are zero
    #     if V_c == 0 or V_p1 == 0:
    #         raise ValueError("Cannot divide by zero")


class TestODE(unittest.TestCase):
    # Still working on this one
    def test_sol(self):
        pass
        # model = {
        #     "name": "model1",
        #     "Q_p1": 1.0,
        #     "V_c": 1.0,
        #     "V_p1": 1.0,
        #     "CL": 1.0,
        #     "X": 1.0,
        # }

        # args = [model["Q_p1"], model["V_c"], model["V_p1"], model["CL"],
        # model["X"]]
        # sol = scipy.integrate.solve_ivp(
        #     fun=lambda t, y: rhs(t, y, *args),
        #     t_span=[t_eval[0], t_eval[-1]],
        #     y0=y0,
        #     t_eval=t_eval,
        # )


# This bit prints the test result in the terminal
if __name__ == "__main__":
    unittest.main()
