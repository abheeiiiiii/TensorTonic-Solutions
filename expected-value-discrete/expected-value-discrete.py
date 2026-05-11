import numpy as np

def expected_value_discrete(x, p):
    x=np.array(x,dtype=float)
    p=np.array(p,dtype=float)

    if x.shape !=  p.shape:
      raise ValueError("shape of x and p must match")

    if not np.isclose(np.sum(p),1.0,atol=1e-6):
        raise ValueError("probalities must sum to 1")

    return float(np.sum(x*p))