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
# SMM
COUNTERS = (
    'CC',
    'ACC',
    'PCC',
    'PACC',
    'X',
    'MAX',
    'T50',
    'MS',
    'HDy',
    'DyS',
    'SORD',
    'SMM',
)

# Define how many iterations each sample from the test portion of the dataset will run. This is to make sure a quantifier doesn't get 'lucky' and is tested with a easier subset
N_ITERATIONS = 1

# Define different test sizes for samples
BATCH_SIZES = [10]

# Define different positive proportions for the samples
ALPHA_VALUES = [round(x, 2) for x in np.linspace(0, 1, 11)]

# Method to measure distance, options are:
# topsoe
# hellinger
# probsymm
MEASURE = 'topsoe'
