import sympy as smp
from sympy import symbols,diff
import numpy as np

## bisection method

import math
from datetime import datetime
# def f(x):
    # return x**3-3*x+5
# for u in range(-5,0):
#     for v in range(-5,5):
#         if abs(u-v)==1 and f(u)*f(v)<0:
#             a=u
#             b=v
# print(a,b)
# a=int(input('Enter start point of interval:\n'))
# b=int(input('Enter end point of interval:\n'))
# z=int(input('Enter the required significant points:\n'))
# e=10**(-z)
# i=math.ceil(math.log(abs(b-a)/e,2))
# if f(a)*f(b)>0:
#     print(f"Bisection fails in the interval [{a},{b}]")
# print("number of iterations:",i)
# t_i= datetime.now()
# n=0
# while n<i:
#     mid=(a+b)/2
#     err=abs(b-a)
#     print(f'at iteration {i} approximate root is mid and error is {err}')

#     if f(a)*f(mid)<0:
#         b=mid
#     elif f(mid)*f(b)<0:
#         a=mid
#     print(f"iteration {n}",mid)
#     n+=1
# t_f= datetime.now()
# print("cost of computtation:",t_f-t_i)

# ## Newton Raphson

'''the difference in the use of library change the number of iteration required for the results.
Lambdify library considers the integer value of the derivative which reduces the number 
of iterations
 whereas subs command takes float value to find accurate results, increasing 
 the number of iterations.'''

# x0=int(input('enter initial value:\n'))
# z=int(input('enter tolerance:\n'))
# e=10**(-z)
# x=symbols('x')
# def f(x):
#     return x**3-3*x+5
# itime=datetime.now()
# dfdx=diff(f(x),x)
# dfdx_val=smp.lambdify(x,dfdx)
# if dfdx_val(x0)!=0:
#     h=((f(x0))/dfdx_val(x0))
#     i=0
#     while abs(h)>=e:
#         h=((f(x0))/dfdx_val(x0))
#         x1=x0-h
#         print(f'iteration {i+1}',x1)
#         x0=x1
#         i+=1
#     ftime=datetime.now()
#     print(f'The root of {f(x)} is :',x1)
#     print("cost of computation",ftime-itime)

## Newton Raphson with multiplicity

# x0=int(input('enter initial value:\n'))
# z=int(input('enter tolerance:\n'))
# m=int(input('enter multiplicity:\n'))
# e=10**(-z)
# x=symbols('x')
# def f(x):
#     return x**2-2*x+1
# dfdx=diff(f(x),x)
# dfdx_val=smp.lambdify(x,dfdx)
# if dfdx_val(x0)!=0:
#     h=((f(x0))/dfdx_val(x0))
#     i=0
#     while abs(h)>=e:
#         if dfdx_val(x0)!=0:
#             h=((f(x0))/(dfdx_val(x0)))
#             x1=x0-m*h
#             print(f'iteration {i+1}',x1)
#             x0=x1
#         i+=1
#     print(f'The root of {f(x)} is :',x1)

## Newton Raphson without multiplicity

# x0=int(input('enter initial value:\n'))
# z=int(input('enter tolerance:\n'))
# e=10**(-z)
# x=symbols('x')
# def f(x):
#     return x**2-2*x+1
# dfdx=diff(f(x),x)
# dfdx_val=smp.lambdify(x,dfdx)
# if dfdx_val(x0)!=0:
#     h=((f(x0))/dfdx_val(x0))
#     i=0
#     while abs(h)>=e:
#         if dfdx_val(x0)!=0:
#             g=f(x)/dfdx
#             dgdx=diff(g,x)
#             dgdx_val=smp.lambdify(x,dgdx)
#             h=((f(x0))/(dfdx_val(x0)*dgdx_val(x0)))
#             x1=x0-h
#             print(f'iteration {i+1}',x1)
#             x0=x1
#         i+=1
#     print(f'The root of {f(x)} is :',x1)

## Regula-Falsi

# a=int(input('enter starting interval:\n'))
# b=int(input('enter ending interval:\n'))
# z=int(input('enter required significant digits:\n'))
# e=10**(-z)
# def f(x):
#     return x**3-3*x+5
# itime=datetime.now()
# i=1
# while i>e:

#     p= (a*f(b)-b*f(a))/(f(b)-f(a))
#     i=abs(p-b)
    #   print(f'for approximate root p the error is {i}')
#     if f(a)*f(p)<0:
#         b=p
#     elif f(p)*f(b)<0:
#         a=p
#     ftime=datetime.now()
#     print(f"iteration {z}",p)
# print("cost of computation",ftime-itime)

## secant method
    
# a=int(input('enter starting interval:\n'))
# b=int(input('enter ending interval:\n'))
# z=int(input('enter required significant digits:\n'))
# e=10**(-z)
# def f(x):
#     return x**3-3*x+5
# itime=datetime.now()
# z=1
# while z>e and (f(b)-f(a))!=0:
#     p= b - (f(b)*((b-a)/(f(b)-f(a))))
#     err = abs(p-b)
#     print(f'for approximate root p the error is {err}')
#     print(p)
#     a=b
#     b=p
# ftime=datetime.now()
# print("cost of computation",ftime-itime)



## Newton Non- linear

# x=symbols('x')
# y=symbols('y')

# u=(x**3)-(3*x*(y**2))+1
# v=-y**3+(3*(x**2)*(y))

# x=int(input('enter the initial point x'))
# y=int(input('enter the initial point y'))
# n=int(input('enter number of iterations'))

# dudx=smp.lambdify([x,y],diff(u,x))
# dudy=smp.lambdify([x,y],diff(u,y))
# dvdx=smp.lambdify([x,y],diff(v,x))
# dvdy=smp.lambdify([x,y],diff(v,y))
# u_val=smp.lambdify([x,y],u)
# v_val=smp.lambdify([x,y],v)

# i=0
# while i<n:
#     J= np.array([[dudx(x,y),dudy(x,y)],[dvdx(x,y),dvdy(x,y)]])
#     P=np.array([u_val(x,y),v_val(x,y)])
#     inv_J=np.linalg.inv(J)
#     ans=np.dot(inv_J,-P)
#     x=ans[0]
#     y=ans[1]
#     print(ans)
#     i+=1


# n=5
# k=0.005125
# h=0.1
# s=float(k/h**2)
# A=np.empty(n,dtype=float)
# for i in range(n):
#     for j in range(n):
#         # if i==j:
#             # A[i][j]=1-2*s
#             A[i+1][j]=s
#             A[i][j-1]=s
# print(s)


