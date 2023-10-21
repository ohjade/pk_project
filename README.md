# PKModel

PKModel is a Python library for specifying, solving, and visualizing the solutions of pharmacokinetic (PK) models. It provides a flexible framework for modeling the distribution and elimination of drugs in the body.

## Pharmacokinetic Modelling
The field of Pharmacokinetics (PK) provides a quantitative basis for describing the delivery of a drug to a patient, the diffusion of that drug through the plasma/body tissue, and the subsequent clearance of the drug from the patient's system. PK is used to ensure that there is sufficient concentration of the drug to maintain the required efficacy of the drug, while ensuring that the concentration levels remain below the toxic threshold (See Fig 1). Pharmacokinetic (PK) models are often combined with Pharmacodynamic (PD) models, which model the positive effects of the drug, such as the binding of a drug to the biological target, and/or undesirable side effects, to form a full PKPD model of the drug-body interaction. This project will only focus on PK, neglecting the interaction with a PD model.

![pk1](https://github.com/ohjade/pk_project/assets/120578702/7ddb0c20-eb49-4cdb-a861-ee9a597b29fb)

PK enables the following processes to be quantified:
    - Absorption
    - Distribution
    - Metabolism
    - Excretion

These are often referred to as ADME, and taken together describe the drug concentration in the body when medicine is prescribed. These ADME processes are typically described by zeroth-order or first-order rate reactions modelling the dynamics of the quantity of drug qq, with a given rate parameter kk, for example:

$$dq/dt=-k*,$$
$$dq/dt=-kq$$

The body itself is modelled as one or more compartments, each of which is defined as a kinetically homogeneous unit (these compartments do not relate to specific organs in the body, unlike Physiologically based pharmacokinetic, PBPK, modeling). There is typically a main central compartment into which the drug is administered and from which the drug is excreted from the body, combined with zero or more peripheral compartments to which the drug can be distributed to/from the central compartment (See Fig 2). Each peripheral compartment is only connected to the central compartment.

![pk2](https://github.com/ohjade/pk_project/assets/120578702/e146e1b2-1b67-4240-95c9-6ac7a8224aad)


## Installation

Install the library using pip:

```bash
pip install -i https://test.pypi.org/simple/ pkmodel-stupiders
```
## Running the model
Specify the model parameters by changing the arguments of the Model class
A description of each of the parameters is given in model.py

`default = Model("default", 2, "intravenous", [1, 2], 1, [1, 2], 1, 1, 1)`

Generate the plot simply by passing your model to the plot class
`plot = Plot(default)`

## API Documentation

### Model Class

The `Model` class represents a pharmacokinetic model. It provides methods for specifying and solving the model.

#### `Model.__init__(...)`

Initialize a new pharmacokinetic model.

Parameters:
1. The dose function Dose(t), which could consist of instantaneous doses of X ng of the drug at one or more time points, or a steady application of X ng per hour over a given time period, or some combination.
2. Vc [mL], the volume of the central compartment
3. Vp1 [mL], the volume of the first peripheral compartment
4. CL [mL/h], the clearance/elimination rate from the central compartment
5. Qp1  [mL/h], the transition rate between central compartment and peripheral compartment 1

Example:

```python
import pkmodel

# Create a two-compartment model
model = pkmodel.Model(...)
```

## Testing
Run tests with `python -m unittest <path/to/test.py>`

## License

PKModel is licensed under the [MIT License](https://opensource.org/licenses/MIT).


## Authors and Maintainer

- **Authors:** Jamie, Yang, Jade, Lucy, Douglas
- **Maintainer:** Martin Robinson
- **Maintainer Email:** [martin.robinson@cs.ox.ac.uk](mailto:martin.robinson@cs.ox.ac.uk)
  

## Acknowledgments

- This library is built on the foundation of [Scipy](https://www.scipy.org/) , [Matplotlib](https://matplotlib.org/) and [Numpy](https://numpy.org/)
- Special thanks to contributors and users who have provided valuable feedback.


