"""
This module handles all fingerprinting functions for FANTASTX.
Functionality is implemented in two classes:
    
- `DistanceCalculator`
- `Comparator`

The `DistanceCalculator` class contains methods to assess the
distance between two fingerprint vectors. It is essentially
a wrapper for the sklearn distance metrics. Currently, it is used
for the following fingerprints:

- Many-Body Tensor Representation (`mbtr`)
- Ewald Sum Matrix (`ewald-sum-matrix`)
- Sine Matrix (`sine-matrix`)

!!! Important "Take Notice"
    
    The `DistanceCalculator` class is not useful for fingerprints which
    need more sophisticated or otherwise specialized methods of distance
    comparison. These are:

    - Bag of Bonds (`bag-of-bonds`)
    - SOAP (`rematch-soap` and `average-soap`)
    - Valle-Oganaov (`valle-oganov`)

The `Comparator` class contains methods to create fingerprints for
structures, calculate the distance between the fingerprints of
different structures, and return appropriate flags to selection
algorithms. At a later date, functionality will also be added to
interface with a separate package which handles the calculation
of on-the-fly machine learning force fields.

---

"""