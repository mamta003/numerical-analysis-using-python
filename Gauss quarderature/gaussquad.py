import sympy as smp
from sympy import symbols, Eq, solve, simplify
import numpy as number_of_pointsp

def gauss(f,lower_limit,upper_limit,number_of_points):
    p=(lower_limit+upper_limit)/2
    q=(upper_limit-lower_limit)/2
    if number_of_points==2:
        x=[-0.57735027,0.57735027]
        w=[1,1]
    if number_of_points==3:
        x=[0,0.77459667,-0.77459667]
        w=[0.88888889,0.88888889,0.55555556]
    rslt=0
    for i in range(number_of_points):
        rslt=rslt+(w[i]*f(p+q*x[i]))
    rslt=rslt*q    
    print(rslt)