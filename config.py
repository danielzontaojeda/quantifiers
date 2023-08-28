import numpy as np

# Define which counters to use, the options are:
# CC
# ACC
# PCC
# PACC
# X
# MAX
# T50
# MS
# HDy
# DyS
# SORD
# COUNTERS = ("CC", "ACC", "PCC", "PACC", "X", "MAX", "T50", "MS", "HDy", "DyS", "SORD")
COUNTERS = ("HDy", "DyS", "SORD")

# Define how many iterations each sample from the test portion of the dataset will run. This is to make sure a quantifier doesn't get 'lucky' and is tested with a easier subset
N_ITERATIONS = 3

# Define different test sizes for samples
BATCH_SIZES = [300]

# Define different positive proportions for the samples
ALPHA_VALUES = [round(x, 2) for x in np.linspace(0, 1, 11)]

# TODO: adicionar descrição
MEASURE = "topsoe"
