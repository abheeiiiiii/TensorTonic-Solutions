import numpy as np

def dropout(x, p=0.5, rng=None):
    x = np.array(x, dtype=float)
    
    if p == 0:
        return x, np.ones_like(x)
    
    if rng is None:
        rand = np.random.random(x.shape)
    else:
        rand = rng.random(x.shape)
    
    mask = (rand < (1 - p)).astype(float)
    scale = 1.0 / (1 - p)
    
    dropout_pattern = mask * scale
    output = x * dropout_pattern
    
    return output, dropout_pattern