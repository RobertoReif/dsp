# Matrix Algebra

import numpy as np
#import pandas as pd


A = np.array([[1,2,3],[2,7,4]])
B = np.array([[1,-1],[0,1]])
C = np.array([[5,-1],[9,1],[6,0]])
D = np.array([[3,-2,-1],[1,2,3]])

u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])
w = np.array([1,8,0,5])

# Question 1
print ('Question 1')
print(A.shape)
print(B.shape)
print(C.shape)
print(D.shape)
print(u.shape)
print(v.shape)
print(w.shape)

# Question 2
print ('Question 2')
print(u+v)
print(u-v)
print(6*u)
print(u*v)
print(np.linalg.norm(u))
print(np.sqrt(36+4+9+25))

# Question 3
print('Question 3')
#print(A+C) not defined size of matrix do not match
print(A-np.transpose(C))
print(np.transpose(C)+3*D)
print(np.dot(B,A))
#print(np.dot(B,np.transpose(A))) not defined size of matrix do not match

# Optional
print('Optional')
#print(np.dot(B,C)) not defined
print(np.dot(C,B))
print(np.dot(np.dot(B,B),np.dot(B,B)))
print(np.dot(A,A.transpose()))
print(np.dot(D.transpose(),D))

