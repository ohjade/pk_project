# PKModel

PKModel is a Python library for specifying, solving, and visualizing the solutions of pharmacokinetic (PK) models. It provides a flexible framework for modeling the distribution and elimination of drugs in the body.

## Installation

Install the library using pip:

```bash
pip install -i https://test.pypi.org/simple/ pkmodel-stupiders==1.0.0
```


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
## License

PKModel is licensed under the [MIT License](https://opensource.org/licenses/MIT).


## Authors and Maintainer

- **Authors:** Jamie, Yang, Jade, Lucy, Douglas
- **Maintainer:** Martin Robinson
- **Maintainer Email:** [martin.robinson@cs.ox.ac.uk](mailto:martin.robinson@cs.ox.ac.uk)
  

## Acknowledgments

- This library is built on the foundation of [Scipy](https://www.scipy.org/) , [Matplotlib](https://matplotlib.org/) and [Numpy](https://numpy.org/)
- Special thanks to contributors and users who have provided valuable feedback.


