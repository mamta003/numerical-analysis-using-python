import numpy as np
from collections import deque

eq= np.array([1,-3,-10,5,22,16])
fact=4
qx=np.empty(len(eq))
qx[0]=eq[0]
i=0
while i<len(eq)-1:
    # if len(qx)<len(eq):
# for i in range(len(eq)):
    qx[i+1]= (qx[i]*fact)+eq[i+1]
    i+=1
print(qx)

eq= np.array([1,-3,-10,5,22,16])
fact=4
qx = deque()
qx.append(eq[0])
while len(qx)>0:
    for i in range(len(eq)-1):
        qx1 = (qx[i]*fact)+eq[i+1]
        qx.append(qx1)
    # qx.pop()
    # print(qx.pop())
# for j in 
print(qx.pop())