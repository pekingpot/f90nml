"""f90nml
   ======

   A Fortran 90 namelist parser and generator.

   :copyright: Copyright 2014 Marshall Ward, see AUTHORS for details.
   :license: Apache License, Version 2.0, see LICENSE for details.
"""
__version__ = '0.8-dev'

# Legacy API
from f90nml.namelist import write

from f90nml.parser import Parser
def read(nml_fname, verbose=False):

    parser = Parser(verbose)
    nml = parser.read(nml_fname)
    return nml
