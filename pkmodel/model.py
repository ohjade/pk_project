#
# Model class
#

class Model:

    def __init__(self, name, ncomp, method, Q_p, V_c, V_p, CL, X, Ka):
        self.name = name
        self.ncomp = ncomp                                                  # no. peripheral compartments
        self.method = method                                                # dosing protocol
        self.Q_p = [Q_p] if not isinstance(Q_p, list) else Q_p              # transition rate between central and peripheral compartment(s)
        self.V_c = V_c                                                      # volume of central compartment
        self.V_p = [V_p] if not isinstance(V_p, list) else V_p              # volume of peripheral compartments(s)
        self.CL = CL                                                        # rate of clearance from central compartment
        self.X = X                                                          # doseage amount
        self.ka = Ka                                                        # dose absorption rate

    def dose(self, t, X):
            return X

