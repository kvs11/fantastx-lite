"""
This module contains functions to conduct multi-objective search.
It contains a pool of structures which contains `Population` and
`Archive` sub-groups. The `Population` group is the primary breeding
pool for genetic operations. The `Archive` group is an elite population
which ensures that the structure search is always conducting genetic
operations with at least one structure on the Pareto front. The
algorithm is steady-state, adding one child structure at a time.

The primary multi-objective search algorithm is epsilon-MOEA.
Citation:
[Deb K, Mohan M, Mishra S. Evol Comput. 2005 Winter;13(4):501-25]
However, until the `Population` sub-group has reached the steady-state
capacity, the `Archive` remains uninitialized, and a linear
selection protocol is used instead. In this protocol, every child
structure is added to the `Population` and is assigned a selection
probability which corresponds to its distance to the minimums of each
objective function. Parents for genetic operations are then chosen
randomly.

Once the `Population` has reached steady-state capacity, full epsilon-MOEA
is employed. For a thorough explanation, see the citation above.

!!! note

Single-objective search is also supported, using the original method
of V.S.C. Kolluru.
"""