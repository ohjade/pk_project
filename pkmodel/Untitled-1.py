#
# Model class
#

class Model:
    def __init__(self, name, ncomp, method, Q_p, V_c, V_p, CL, X, Ka):
        self.name = name
        # no. peripheral compartments
        self.ncomp = ncomp
        # dosing protocol
        self.method = method
        # transition rate between central and peripheral compartment(s)
        self.Q_p = [Q_p] if not isinstance(Q_p, list) else Q_p 
        # volume of central compartment
        self.V_c = V_c
        # volume of peripheral compartments(s)
        self.V_p = [V_p] if not isinstance(V_p, list) else V_p
        # rate of clearance from central compartment
        self.CL = CL
        # doseage amount
        self.X = X
        # dose absorption rate
        self.ka = Ka

    def dose(self, t, X):
        return X


