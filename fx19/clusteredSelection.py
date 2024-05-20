'''
This module contains functions to conduct multi-objective search.
It contains a pool of structures which contains the `"Population"`
sub-group of active models. The `"Population"` further divides the
models into clusters. These clusters are actively used in genetic
operations: mating operations can be conducted which pull models
from the same cluster, or different clusters.

Model selection is governed by non-domination ranking. Each model
is ranked twice:

1. The models are ranked by non-domination within the entire
population. Models within the last ranking tier are considered
to be candidates for replacement.

2. The models are ranked by non-domination within their
respective clusters. This ranking determines their selection
probability, $P$, where $P = exp{(-\mathrm{rank_cluster})}$. Ranking starts
at zero. Selection occurs using a roulette selection method. Models are
chosen at random from the population, and a second random number
is drawn. If the second random number is smaller than their selection
probability, then the model is selected. Otherwise, more random
models are drawn until one is successfully chosen.

Non-domination can be calculated using any of the methods in the `dominance`
module. Currently, the options are either standard Pareto-dominance, or
$\epsilon$-dominance. In the latter dominance mechanism, models are not
allowed to live in the same epsilon box of objective space if they are
structurally similar.

The algorithm is steady-state, adding one child structure at a time.

!!! note
    Single-objective search is also supported, using the original method
    of V.S.C. Kolluru.

!!! note
    Currently only compositional clusters are supported,
    support for hierarchical clusters will be added in a subsequent update.
'''