#
# Model class
#

class Model:

    def __init__(self, name, Q_p1, V_c, V_p1, CL, X):
        self.name = name
        self.Q_p1 = Q_p1
        self.V_c = V_c
        self.V_p1 = V_p1
        self.CL = CL
        self.X = X
      
    def dose(self, t, X):
        return X

    def rhs(self, t, y):
        q_c, q_p1 = y
        transition = self.Q_p1 * (q_c / self.V_c - q_p1 / self.V_p1)
        dqc_dt = Model.dose(self, t, self.X) - q_c / self.V_c * self.CL - transition
        dqp1_dt = transition
        return [dqc_dt, dqp1_dt]
    
    def solve(self):

        import numpy as np
        import scipy.integrate

        t_eval = np.linspace(0, 1, 1000)
        y0 = np.array([0.0, 0.0])

        sol = scipy.integrate.solve_ivp(
            fun=lambda t, y: Model.rhs(self, t, y),
            t_span=[t_eval[0], t_eval[-1]],
            y0=y0, t_eval=t_eval
        )
        return sol
    
class Plot(Model):

    def __init__(self, Model):
        import matplotlib.pylab as plt
        import numpy as np
        import scipy.integrate

        # t_eval = np.linspace(0, 1, 1000)
        # y0 = np.array([0.0, 0.0])

        #fig = plt.figure()
        # for model in [Model.parameters, Model.parameters]:
            #print(list(Model.parameters.values())[1:])
        sol = Model.solve()
        plt.plot(sol.t, sol.y[0, :], label=Model.name + '- q_c')
        plt.plot(sol.t, sol.y[1, :], label=Model.name + '- q_p1')
    

        plt.legend()
        plt.ylabel('drug mass [ng]')
        plt.xlabel('time [h]')
        plt.show()


default = Model("default",1,1,1,1,1)
print(default.name)
pl = Plot(default)

