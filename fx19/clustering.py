"""
This module contains functions to perform compositional or hierarchical clustering. 

Compositional clustering is simpler than hierarchical clustering where models 
are grouped purely based on their atomic composition.This contains functions to 
read in models, assign clusters, and update clusters by removing and adding models.

Hierarchical clustering contains functions to read in models, cluster them into flat 
clusters based on similarity metrics (the distances between models in fingerprint
space) and the user specified clustering method, and return thoseclusters for use in 
ML or GA applications.
"""
