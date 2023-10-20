from model import Model
from plot import Plot

# Example #

# Specify the model parameters by changing the arguments of the Model class
# A description of each of the parameters is given in model.py
default = Model("default", 2, "intravenous", [1, 2], 1, [1, 2], 1, 1, 1)

# Generate the plot simply by passing your model to the plot class
plot = Plot(default)
