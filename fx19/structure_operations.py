"""
This module contains classes which handle all genetic structure
operations for FANTASTX. Four basic types of mutations have been
included:

1. **Basin-hopping**: Perturb a fraction of atoms in a structure, each
 by a random distance in a random direction. Atoms cannot overlap, and
 the distance of perturbation cannot exceed a pre-determined threshhold.
2. **Cut-and-splice**: Take 2 structures, cut each structure along a plane,
 and create a child structure by splicing the left piece of structure A
 with the right piece of structure B.
3. **Composition mutation**: Perturb the composition of a structure by
 either adding or removing atoms. The number of atoms added or removed will
 either be random (up to 3 atoms per species), or will correspond to a set
 composition (e.g. AlO4).
4. **Mating by swap**: Take 2 structures and mate them by randomly combining
 sites from each parent.

All basin-hopping mutations are handled by the basinhopping class.
Other mutations are handled differently depending on the class of the
parent structure. Currently, these parent structures can be:

1. **Clusters** (handled by `Evolve`)
2. **Grain Boundaries** (handled by `gb_ops`)
3. **Surfaces** (handled by `surface_ops`)

!!! important
    **Molecules** are also supported in a limited fashion, as a sub-class
    of clusters. The only structural operation currently implemented
    for molecules is basin-hopping.
"""