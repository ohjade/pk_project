# protocol.py
import numpy as np


class Protocol:
    def evaluate(self, t, y):
        model = self.model
        if model.method == "intravenous":
            return self._intravenous_protocol(t, y)
        elif model.method == "subcutaneous":
            return self._subcutaneous_protocol(t, y)
        else:
            raise ValueError(f"Unsupported dosing method: {model.method}")

    def _intravenous_protocol(self, t, y):
        model = self.model
        q_c = y[0]
        q_p = y[1:]
        transitions = []
        dqp_dts = []
        for i in range(0, model.ncomp):
            next_val = model.Q_p[i] * (q_c / model.V_c - q_p[i] / model.V_p[i])
            transitions.append(next_val)
            dqp_dts.append(transitions[i])

        term1 = model.dose(t, model.X)
        term2 = q_c / model.V_c * model.CL
        dqc_dt = term1 - term2 - np.sum(transitions)

        return [dqc_dt, *dqp_dts]

    def _subcutaneous_protocol(self, t, y):
        model = self.model
        (q0, q_c) = y[0:2]
        q_p = y[2:]
        transitions = []
        dqp_dts = []
        for i in range(0, model.ncomp):
            next_val = model.Q_p[i] * (q_c / model.V_c - q_p[i] / model.V_p[i])
            transitions.append(next_val)
            dqp_dts.append(transitions[i])
        dq0_dt = model.dose(t, model.X) - (model.ka * q0)

        term1 = model.ka * q0
        term2 = q_c / model.V_c * model.CL
        dqc_dt = term1 - term2 - np.sum(transitions)

        return [dqc_dt, *dqp_dts, dq0_dt]
