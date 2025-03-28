import numpy as np
import time
from datetime import datetime
a=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype=np.float64)
b=np.array([[3],[2],[7]],dtype=np.float64)
# a=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype=np.float64)
mat=np.concatenate((a,b),axis=1,dtype=np.float64)
sol=np.empty([len(mat),1])
# sol1=np.empty([len(mat),1])
ech=np.empty([len(mat),len(mat[0])])
order=min(len(mat),len(mat[0]))
a=0
t_i=datetime.now()
while a<len(mat):
    for i in range(a,len(ech)):
        # if mat[i][a]==0:
        #     z=mat[a][a]
        #     if mat[i][a]!=0:
        #         mat[a][a]=mat[i][a] 
        #         mat[i][a]=z
        
        fact=mat[i][a]
        # print(mat)
        for j in range(a,len(ech[1])):
            ech[i][j]=mat[i][j]/fact
    # print('divide\n',ech,'\n')            
    for i in range(a+1,len(ech)):
        for j in range(a,len(ech[1])):
            ech[i][j]=ech[i][j]-ech[a][j]
    # print('final\n',ech,'\n')
    mat=ech
    a+=1
print(ech)

#back substitution
m=len(ech)-1
n=len(ech[0])-1
sol[m]=ech[m][n]
# sol1[m]=ech[m][n]
# for i in range(len(ech)-1-1,-1,-1):mamta 
for i in range(m,-1,-1):
    sol[i] = ech[i][n]
    # for j in range(len(ech[0])-1-1,i,-1):mamta
    for j in range(i+1,n):
        sol[i] = sol[i]-ech[i][j]*sol[j]
print(sol)
t_f=datetime.now()
print("cost of computation:", t_f-t_i)
# sol1[2]=ech[2][n]-ech[2][3]*sol1[3]
# sol1[1]=ech[1][n]-ech[1][2]*sol1[2]-ech[1][3]*sol1[3]
# sol1[0]=ech[0][n]-ech[0][1]*sol1[1]-ech[0][2]*sol1[2]-ech[0][3]*sol1[3]
# print(sol1)
# print(sol)

# ...

# 26x1 + 2x2 + 2x3 = 12.6

# 3x1 + 27x2 + x3 = – 14.3

# 2x1 + 3x2 + 17x3 = 6.0
# path = r"C:\Users\Mamta\Desktop\output\my_file_test.txt"
# sol.to_txt(path)
np.savetxt('test',sol,delimiter="    ")