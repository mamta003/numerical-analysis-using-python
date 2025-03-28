import numpy as np 
import math 
import sympy as smp
from sympy import symbols ,Eq,solve
import matplotlib.pyplot as plt
from datetime import datetime as dt

# straight line Fitting 

def f(a,b,p):
    return a*p + b

a = symbols("a")
b = symbols("b")

x = np.array([1,2,3,4,6,8])
y = np.array ([2.4,3.1,3.5,4.2,5,6])
n = len(x)
q1= np.zeros(n)

print("Number of data points = ",n)
t_i=dt.now()
Ex = sum(x)
print("Ex=",Ex)
Ey = sum(y)
print("Ey =", Ey)
Exy = np.dot(x,y)
print("Exy=",Exy)
Ex2 =np.dot(x,x)
print("Ex2 =",Ex2)

eq1 = Eq((a*Ex+b*n),Ey)
eq2 = Eq((a*Ex2+b*Ex),Exy)
print(eq1) 
print(eq2) 
m = solve((eq1, eq2), (a, b))
# print(m)
a = m[a]
b = m[b]
print("a =", a)
print("b =",b)
print("The best fit straight line is y = (",a,") x +(",b,")")
t_f=dt.now()
print('\ncost of computation:',t_f-t_i)

for i in range(n):
    q1[i] = f(a,b,x[i])
    
print(q1)
print(x)

plt.scatter(x, y, label= "stars", color= "red", 
            marker= "o", s=50)
plt.plot(x,q1,color='g', linewidth =1)
plt.title("Curve plotted using  the given points")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()




# import numpy as np 
# import math 
# import sympy as smp
# from sympy import symbols ,Eq,solve
# import matplotlib.pyplot as plt

# Second degree polynomials Fitting 

def f(a,b,c,p):
    return a*p*p + b*p + c

a = symbols("a")
b = symbols("b")
c = symbols("c")

x = np.array([1,2,3,4,5])
y = np.array ([5,12,26,60,97])
n = len(x)
q1= np.zeros(n)

print("Number of data points = ",n)

t_i=dt.now()
Ex = sum(x)
print("Ex=",Ex)

Ey = sum(y)
print("Ey =", Ey)

Exy = np.dot(x,y)
print("Exy=",Exy)

Ex2 =np.dot(x,x)
print("Ex2 =",Ex2)

Ex3 =sum([num**3 for num in x])
print("Ex3 =",Ex3)

Ex4 =sum([num**4 for num in x])
print("Ex4 =",Ex4)

x2 = [num**2 for num in x]
Ex2y =np.dot(x2,y)
print("Ex2y =",Ex2y)


eq1 = Eq((a*Ex2+b*Ex+c*n),Ey)
eq2 = Eq((a*Ex3+b*Ex2+c*Ex),Exy)
eq3 = Eq((a*Ex4+b*Ex3+c*Ex2),Ex2y)

print(eq1) 
print(eq2) 
print(eq3) 

m = solve((eq1, eq2, eq3 ), (a, b,c))
# print(m)
a = m[a]
b = m[b]
c = m[c]

print("a =", a)
print("b =",b)
print("c = ",c)
print("The best fit of second degree polynomial is y = (",a,")x^2 + (",b,")x + (",c,")")
t_f=dt.now()
print('\ncost of computation:',t_f-t_i)


for i in range(n):
    q1[i] = f(a,b,c,x[i])
    
print(q1)
print(x)

plt.scatter(x, y, label= "stars", color= "red", 
            marker= "o", s=50)
plt.plot(x,q1,color='g', linewidth =1)
plt.title("Curve plotted using  the given points")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

t_f=dt.now()
print('\ncost of computation:',t_f-t_i)

# # # Fitting of Exponential Curve - 

# def f(a,b,p):
#     return b*math.e**((a)*p)

# a = symbols("a")
# b = symbols("b0")


# x = np.array([1,2,3,4,5,6])
# Y = np.array ([1.6,4.5,13.8,40.8,125,300])
# n = len(x)
# y = np.zeros(n)
# y =  [math.log(i) for i in Y]

# # print(y)


# q1= np.zeros(n)

# print("Number of data points = ",n)

# Ex = sum(x)
# print("Ex=",Ex)
# Ey = sum(y)
# print("Ey =", Ey)
# Exy = np.dot(x,y)
# print("Exy=",Exy)
# Ex2 =np.dot(x,x)
# print("Ex2 =",Ex2)

# eq1 = Eq((a*Ex+b*n),Ey)
# eq2 = Eq((a*Ex2+b*Ex),Exy)
# print(eq1) 
# print(eq2) 
# m = solve((eq1, eq2), (a, b))
# # print(m)
# a = m[a]
# b = m[b]
# print("a =", a)
# print("b0 =",b)
# b = math.e**b
# print("b =",b)
# print("The best fit of exponantial curve is y =(,",b,")e^(",a,")x")


# for i in range(n):
#     q1[i] = f(b,a,x[i])
    
# print(q1)
# print(x)

# plt.scatter(x, Y, label= "stars", color= "red", 
#             marker= "o", s=50)
# plt.plot(x,q1,color='g', linewidth =1)
# plt.title("Curve plotted using  the given points")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()