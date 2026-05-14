import numpy as np
import math

def entropy_node(y):
    values, counts = np.unique(y, return_counts=True)
    probabilities = counts / len(y)

    h = 0

    for p in probabilities:
        if p > 0:
            h += -p * math.log2(p)

    return float(h)