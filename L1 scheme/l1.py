import math
import numpy as np

def g(x):
     return x**2

def l1_scheme(a, M, m):    
    t = [m * k for k in range(M)]
    
    d = [(k**(1-a)) - ((k-1)**(1-a)) for k in range(1, M+1)]

    u = np.zeros(M) 
    
    for m in range(1, M):
        if m == 1:
            u[m] = (1 / d[0]) * ((math.gamma(2-a) / 1) * g(t[m]) + d[m-1] * u[0])
        else:
            summation = sum((d[k] - d[k-1]) * u[m-k] for k in range(1, m))
            u[m] = (1 / d[0]) * ((math.gamma(2-a) / 1) * g(t[m]) + d[m-1] * u[0] - summation)
    
    return t, u

a = 0.5  
M = 6    
m = 0.2 
t, u = l1_scheme(a, M, m)

for i in range(len(t)):
    print(f"t={t[i]:.2f}, u={u[i]:.6f}")
