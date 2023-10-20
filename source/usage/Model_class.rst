===========
Model Class
===========

The Model class represents a pharmacokinetic model. It provides methods for specifying and solving the model.

-------------------
Model.__init__(...)
-------------------
Initialize a new pharmacokinetic model.


Parameters:
-----------
parameters:

* The dose function Dose(t), which could consist of instantaneous doses of X ng of the drug at one or more time points, or a steady application of X ng per hour over a given time period, or some combination.
* Vc [mL], the volume of the central compartment
* Vp1 [mL], the volume of the first peripheral compartment
* CL [mL/h], the clearance/elimination rate from the central compartment
* Qp1 [mL/h], the transition rate between central compartment and peripheral compartment 1


Example:

..example-code:: python

import pkmodel

# Create a two-compartment model
model = pkmodel.Model(...)
