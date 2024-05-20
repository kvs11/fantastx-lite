"""
This module performs relaxations and then populates the following data for
a model using either VASP or LAMMPS. OTher energy codes can be implemented 
following the similar code structure - 

1. evaluate_energy : does structure relaxation, and gives energy

2. energy_obj : The first objective function (energy) is calculated
"""