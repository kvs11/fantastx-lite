'''
This module contains all methods to calculate dominance relationships of
FANTASTX models. Currently, two dominance methods are implemented:

1. **Pareto dominance** (`ParetoDominance`): model A dominates model B if all
 of it's objective values are better than model B's (or vice-versa for model
 B dominating model A). It is non-dominated with B if at least one of its
 objective values is better than B's, but at least one of B's objective
 values is better than A's. 
2. **Epsilon dominance** (`EpsilonDominance`): same as Pareto dominance, but
 now the objective value space is discretized into $\epsilon$ grid boxes.
 Non-dominance is checked based on the corner (given by the floor or ceiling
 of each objective if minimizing or maximizing said objective) of the
 $\epsilon$ box that the model occupies. In the [original]()
 implementation, models were not allowed to occupy the same $\epsilon$ box,
 and the model that was kept was the model whose objective values were closest
 to the (possibly hyperdimensional) box corner. Here, the calculation of the
 distance to the box corner is kept, but models but only to determine
 dominance of models occupying the same box.

Both dominance methods have been further modified to facilitate
model structural comparisons. These structural comparisons are automatically
made if a `Comparator` object is provided to the dominance class. To enhance
efficiency, functionality has been included to only make structural
comparisons with other models whose objectives all lie within an $\epsilon$
box centered on the target model's objectives. This will always be the case
for `EpsilonDominance`, where these "structural" $\epsilon$ values will be
the same as those used for dominance calculations. For `ParetoDominance`,
these $\epsilon$ values need to be provided separately. If none are provided,
then structural comparisons are made with all other models.
'''