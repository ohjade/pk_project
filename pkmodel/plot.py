# plot.py
import matplotlib.pylab as plt
from solution import Solver


class Plot:
    def __init__(self, model):
        solver = Solver(model)
        sol = solver.solve_ivp()

        plt.plot(sol.t, sol.y[0, :], label=model.name + "- q_c")
        for i in range(0, model.ncomp):
            plt.plot(sol.t, sol.y[1 + i, :], label=model.name + f"- q_p{i}")
        if model.method == "subcutaneous":
            plt.plot(sol.t, sol.y[-1, :], label=model.name + "- q0")

        plt.legend()
        plt.ylabel("drug mass [ng]")
        plt.xlabel("time [h]")
        plt.show()
