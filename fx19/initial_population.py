"""
This module contains classes to make the initial models that FANTASTX
will seed the evolutionary algorithm with. Two types of initial models
are supported:

1. Models that use user-provided structures
2. Models that use random structures. It should be noted that this
 method of random model generation is only useful for clusters and bulk
 geometries. Grain boundaries and surfaces have their own unique methods
 of creating random structures, which can be found in the
 [`structure_operations`](../structure_operations-reference/) class.

 ---
"""