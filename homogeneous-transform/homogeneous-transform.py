import numpy as np

def apply_homogeneous_transform(T, points):
    points = np.array(points, dtype=float)
    single = points.ndim == 1
    
    if single:
        points = points.reshape(1, 3)
    
    ones = np.ones((points.shape[0], 1))
    points_h = np.hstack((points, ones))
    
    transformed = (T @ points_h.T).T
    
    result = transformed[:, :3]
    
    return result[0] if single else result