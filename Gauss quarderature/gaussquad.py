import sympy as smp
from sympy import symbols, Eq, solve, simplify
import numpy as np

def gauss(f, lower_limit, upper_limit, number_of_points):
    p = (lower_limit + upper_limit) / 2
    q = (upper_limit - lower_limit) / 2

    if number_of_points == 2:
        x = [-0.57735027, 0.57735027]
        w = [1, 1]
    elif number_of_points == 3:
        x = [0, 0.77459667, -0.77459667]
        w = [0.88888889, 0.55555556, 0.55555556]
    else:
        print("Only 2 or 3 point Gaussian quadrature supported!")
        return None

    rslt = 0
    for i in range(number_of_points):
        rslt += w[i] * f(p + q * x[i])
    
    rslt *= q
    print("Approximate integral:", rslt)

f = lambda x: x**2  
gauss(f, 0, 1, 2)  
