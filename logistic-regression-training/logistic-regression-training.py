import numpy as np

def _sigmoid(z):
    return 1 / (1 + np.exp(-z))

def train_logistic_regression(X, y, lr, steps):
    X = np.array(X, dtype=float)
    y = np.array(y, dtype=float)
    
    N, D = X.shape
    
    w = np.zeros(D)
    b = 0.0
    
    for _ in range(steps):
        z = X @ w + b
        p = _sigmoid(z)
        
        dw = (1/N) * (X.T @ (p - y))
        db = (1/N) * np.sum(p - y)
        
        w -= lr * dw
        b -= lr * db
    
    return w, b