import numpy as np
import sympy as smp
from sympy import symbols, Eq, solve, simplify
import math
from datetime import datetime
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import time

# ## newton forward difference

# x=np.array([1891,1901,1911,1921,1931])
# y=np.array([46,66,81,93,101])
# # n= int(input('Enter the number of data points:\n'))
# # p=float(input('Enter the evaluation point of data:\n'))
# # x=np.empty(n)
# # x[0]=int(input("enter initial data point:\n"))
# n=len(x)
# h=10
# p=1895
# # u=(p-x0)/h 
# u=symbols('u')
# rslt = np.zeros([n,n+1])
# for k in range(n):
#     rslt[k][0]=x[k]
#     rslt[k][1]=y[k]
# print('Initializing the resultant matrix:\n',rslt,'\n')
# a=n-1
# j=2
# while j<n+2:
#     i=0
#     while i<a:
#         rslt[i][j]=((rslt[i+1][j-1]-rslt[i][j-1]))
#         i+=1
#     a-=1
#     j+=1
# print('The resultant matrix is:\n',rslt,'\n')
# j=2
# sum=rslt[0][1]
# while j<n+1:
#     partition=rslt[0][j]
#     k=0
#     while k<j-1:
#         partition = partition* (u-(k))
#         k+=1
#     # print(partition)
#     sum+=partition/math.factorial(j-1)
#     j+=1
# print(f'The polynomial is:\n',sum,'\n')
# poly=smp.lambdify(u,sum)
# print(f"The simplified value of the polynomial is:\n",simplify(sum),'\n')
# u = (p-x[0])/h
# print(f'The value of polynomial at {p} is:\n',poly(u),'\n')

# ## newton backward difference

# x=np.array([0,1,2,3,4])
# y=np.array([5,8,12,17,26])
# p=4
# n=len(x)
# # rslt = np.zeros([n,n+2])
# # for k in range(n):
# #     rslt[k][0]=rslt[k][0]+x[k]
# #     rslt[k][1]=rslt[k][1]+y[k]

# # n= int(input('Enter the number of data points:\n'))
# # p=float(input('Enter the evaluation point of data:\n'))
# # x[0]=int(input("enter initial data point:\n"))
# h=1
# u=(p-x[0])/h 
# u=symbols('u')
# rslt = np.zeros([n,n+2])
# for k in range(n):
#     rslt[k][0]=x[k]
#     # rslt[k][1]=input('Enter the functional value at given point x:\n')
#     rslt[k][1]=y[k]
# print('Initializing the resultant matrix:\n',rslt,'\n')

# j=2
# while j<n+2:
#     a=j-1
#     i=n-1
#     while i>a-1:
#         rslt[i][j]=((rslt[i][j-1]-rslt[i-1][j-1]))
#         i-=1
#     a-=1
#     j+=1
# print('The resultant matrix is:\n',rslt,'\n')
# j=2
# sum=rslt[n-1][1]
# while j<n:
#     partition=rslt[n-1][j]
#     k=0
#     while k<j-1:
#     # for k in range(j-1):
#         partition = partition* (u+(k))
#         k+=1
#     # print(partition)
#     sum+=partition/math.factorial(j-1)
#     j+=1
# print(f'The polynomial is:\n',sum,'\n')
# poly=smp.lambdify(u,sum)
# print(f"The simplified value of the polynomial is:\n",simplify(sum),'\n')
# u = (p-rslt[n-1][0])/h
# # print(u)
# print(f'The value of polynomial at {p} is:\n',poly(p),'\n')