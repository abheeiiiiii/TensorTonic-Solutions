def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    x=x0
    i=steps
    for _ in range (i):
     grad= 2*a*x + b
     x= x-lr*grad
    return float(x)