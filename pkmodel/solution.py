# solution.py
import numpy as np
import scipy
from pkmodel.protocol import Protocol


class Solver:
    def __init__(self, model):
        self.model = model

    def rhs(self, t, y):
        protocol_instance = Protocol()
        protocol_instance.model = self.model
        return protocol_instance.evaluate(t, y)

    def solve_ivp(self):
        t_eval = np.linspace(0, 1, 1000)
        y0 = np.zeros(self.model.ncomp + 1)
        if self.model.method == "subcutaneous":
            y0 = np.zeros(self.model.ncomp + 2)

        sol = scipy.integrate.solve_ivp(
            fun=lambda t, y: self.rhs(t, y),
            t_span=[t_eval[0], t_eval[-1]],
            y0=y0,
            t_eval=t_eval,
        )
        return sol
