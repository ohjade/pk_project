#
# Model class
#

class Model:

    def __init__(self, name, ncomp, method, Q_p, V_c, V_p, CL, X, Ka):
        self.name = name
        self.ncomp = ncomp          # no. peripheral compartments
        self.method = method        # dosing protocol
        self.Q_p = Q_p              # transition rate between central and peripheral compartment(s)
        self.V_c = V_c              # volume of central compartment
        self.V_p = V_p              # volume of peripheral compartments(s)
        self.CL = CL                # rate of clearance from central compartment
        self.X = X                  # doseage amount
        self.ka = Ka                # dose absorption rate

    def dose(self, t, X):
            return X

    def rhs(self, t, y):
        import numpy as np
        if self.method == "intravenous":
            q_c = y[0]
            q_p = y[1:]
            transitions = []
            dqp_dts = []
            for i in range(0, self.ncomp):
                transitions.append(self.Q_p[i] * (q_c / self.V_c - q_p[i] / self.V_p[i]))
                dqp_dts.append(transitions[i])
            dqc_dt = Model.dose(self, t, self.X) - q_c / self.V_c * self.CL - np.sum(transitions)
            
            return [dqc_dt, *dqp_dts]
        
        if self.method == "subcutaneous":
            q0, q_c, = y [0:2]
            q_p = y[2:]           
            transitions = []
            dqp_dts = []
            for i in range(0, self.ncomp):
                transitions.append(self.Q_p[i] * (q_c / self.V_c - q_p[i] / self.V_p[i]))
                dqp_dts.append(transitions[i])
            dq0_dt = Model.dose(self, t, self.X) - (self.ka * q0)
            dqc_dt =( self.ka * q0) - q_c / self.V_c * self.CL - np.sum(transitions)

            return [dqc_dt, *dqp_dts, dq0_dt]

    
    def solve(self):

        import numpy as np
        import scipy.integrate
    
        t_eval = np.linspace(0, 1, 1000)
        y0 = np.zeros(self.ncomp + 1)           # set initial concentrations in all compartments to 0
        if self.method == "subcutaneous":       # add extra compartment for drug absorption to main compartment
            y0 = np.zeros(self.ncomp + 2)       # need at least 2, one central, one q0 and then peripheral compartments

        sol = scipy.integrate.solve_ivp(
            fun=lambda t, y: Model.rhs(self, t, y),
            t_span=[t_eval[0], t_eval[-1]],
            y0=y0, t_eval=t_eval
        )
        return sol
    
class Plot(Model):

    def __init__(self, Model):
        import matplotlib.pylab as plt

        sol = Model.solve()
        
        plt.plot(sol.t, sol.y[0, :], label=Model.name + '- q_c')
        for i in range(0, Model.ncomp):
            plt.plot(sol.t, sol.y[1 + i, :], label=Model.name + f'- q_p{i}')
        if Model.method == "subcutaneous":
            plt.plot(sol.t, sol.y[-1, :], label=Model.name + '- q0')
    

        plt.legend()
        plt.ylabel('drug mass [ng]')
        plt.xlabel('time [h]')
        plt.show()


# default = Model("default",1,"subcutaneous",1,1,1,1,1,1)
# default = Model("default",3,"subcutaneous",[1,2,5],1,[1,2,3],1,1,1)
# pl = Plot(default)

