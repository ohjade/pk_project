"""pkmodel is a Pharmacokinetic modelling library.

It contains functionality for creating, solving, and visualising the solution
of Pharmacokinetic (PK) models

"""
# Import version info
from .version_info import VERSION_INT, VERSION  # noqa

# Import main classes
from .model import Model    # noqa
from .protocol import Protocol    # noqa
from .solution import Solution     # noqa
