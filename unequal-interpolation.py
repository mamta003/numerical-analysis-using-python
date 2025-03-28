import numpy as np
import sympy as smp
from sympy import symbols, Eq, solve, simplify
import math
from datetime import datetime
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import time

#  lagrange
x = np.array([0,2,4,8])
y = np.array([3,8,11,19])
z=2.5
a=symbols('a')
i=1
n=len(x)
b=0
t_i = datetime.now()
while i < 4:
    p=1
    j=0
    while j < n:
    # for j in range(n):
        if i!=j:
            p=p*(a-x[j])/(x[i]-x[j])
        j+=1
    b+=y[i]*p
    i+=1
t_f = datetime.now()
poly= smp.lambdify(a,b)
print('The cost of computation is:\n',t_f-t_i)
# print(f'poly:\n',simplify(poly))
print('The interpolating polynomial is : \n',simplify(b), '\nThe value of the function is:\n',poly(z))

# # ##newton divided difference
# x= np.array([0,2,4,8])
# y=np.array([3,8,11,19])
# z=2
# n=len(x)
# rslt= np.zeros([n,n+2-1])

# for k in range(n):
#     rslt[k][0]=rslt[k][0]+x[k]
#     rslt[k][1]=rslt[k][1]+y[k]
# print('initial\n',rslt)
# j=2
# a=n-1
# p=symbols('p')
# while j<n+2-1:
#     i=0
#     k=j-1
#     while i<a:
#         d=rslt[i+k][0]-rslt[i][0]  
#         rslt[i][j]=rslt[i][j]+((rslt[i+1][j-1]-rslt[i][j-1])/d)
#         i+=1
#     a-=1
#     k+=1
#     j+=1
# print(f'The table with col1 as x and col2 and function\n',rslt,'\n')

# j=2
# sum=y[0]
# while (j<n+2-1):
#     partition=rslt[0][j]
#     i=0
#     while i<j-1:
#         partition = partition*(p-x[i])
#         i+=1
#     sum+=partition
#     j+=1
# print('The required polynomial is\n',simplify(sum),'\n')  
# poly=smp.lambdify(p,sum)
# # print('actual polt\n',)
# print(f'The value of polynomial at {z} is \n',poly(z))
