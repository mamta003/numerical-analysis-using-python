import numpy as np
import sympy as smp
from sympy import symbols, Eq, solve, simplify
import math
from datetime import datetime
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import time

# # Trapizoidal

# a = 0
# b = 3
# n = 6
# x0 = 0
# h = abs((b-a)/n)
# def f(x):
#     return (2*x-(x**2))Z
# y = np.empty(n+1)
# y[0]=f(a)
# y[n]=f(b)
# # for i in range(n+1):
# i=1
# sum = h*((f(x0)+f(x0+n*h))/2)
# while i<n:
#     y[i] = f(x0+i*h)
#     sum =  sum + h*f(x0+i*h)
#     i+=1
# print(y)
# print(sum)

# # simpson's 1/3

# a = 0
# b = 3
# n = 6
# x0 = 0
# h = (b-a)/n

# def f(x):
#     return (2*x-(x**2))
# y = np.empty(n+1)
# y[0]=f(a)
# y[n]=f(b)
# i=1
# sum = ((f(x0)+f(x0+n*h)))
# p=0
# q=0
# while i<n:
#     y[i] = f(x0+i*h)
#     if i%2==0:
#         p+=2*(y[i])
#     else:
#         q+=4*(y[i])
#     i+=1
# print(y)
# sum =  (h/3)*(sum + p+q)
# print(f"\nthe value of the given integral by Simpson's is \n {sum}")


# # simpson's 3/8

# a = 0
# b = 1
# n = 6
# x0 = 0
# h = (b-a)/n

# def f(x):
#     return 1/(1+x)
# y = np.empty(n+1)
# y[0]=f(a)
# y[n]=f(b)
# i=1
# sum = ((f(x0)+f(x0+n*h)))
# p=0
# q=0
# while i<n:
#     y[i] = f(x0+i*h)
#     if i%3==0:
#         p+=2*(y[i])
#     else:
#         q+=3*(y[i])
#     i+=1
# print(y)
# sum =  (3*h/8)*(sum + p+q)
# print(f"\nthe value of the given integral by Simpson's is \n {sum}"