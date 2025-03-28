import numpy as np
from collections import deque

eq= np.array([1,-2.2790,2.1938])
z=20 #number of iterations
for i in range(z):
    p0=2.2790
    q0=-2.1938
    ans=np.empty((2,len(eq)))

    for j in range(2):
        qx = np.empty(len(eq))
        qx[0]=eq[0]
        for i in range(len(eq)-1):
            if i==0:
                qx[i+1] = (qx[i]*p0)+eq[i+1]
            qx[i+1] = (qx[i]*p0)+ (qx[i-1]*q0) +eq[i+1]
        ans[j]=qx
        eq=qx
    b=ans[0]
    c=ans[1]
    n=len(eq)-1
    dp=-((b[n]*c[n-3])-(b[n-1]*c[n-2]))/((c[n-2]**2) -(c[n-3]*(c[n-1]-b[n-1])))
    dq=-(b[n-1]*(c[n-1]-b[n-1])-b[n]*c[n-2])/((c[n-2]**2)-c[n-3]*(c[n-1]-b[n-1]))
    # print(b[n-1]*(c[n-1]-b[n-1])-b[n]*c[n-2])
    p1=p0+dp
    q1=q0+dq
    p0=p1
    q0=q1
    # print(ans)
    print(p1,q1)