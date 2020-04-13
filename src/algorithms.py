import copy
from math import sqrt

import numpy as np

def dot_product(a, b):
    c = 0.0
    if len(a)!=0:
        for i in range(len(a)):
            c += a[i] * b[i]
        return c
    else:
        return c

def dot_product_matrix(a, b):
    c = []
    c.append([])
    if len(a)!=0:
        for i in range(len(a)):
            c[0].append(0)
            x=0
            for j in range(len(a)):
                x += a[i][j] * b[0][j]
            c[0][i]=x
        return c
    else:
        return c


def norm(M):
    sum=0
    for i in range(len(M[0])):
        sum+=M[0][i]*M[0][i]
    return sqrt(sum)

def multiply(a,V1):

    V=copy.copy(V1)
    for i in range(len(V)):
        V[i]=a*V[i]
    return V

def add(AA,B):
    A=copy.copy(AA)
    for i in range(len(A)):
        A[i]+=B[i]
    return A

def sub(AA,B):
    A = copy.copy(AA)
    for i in range(len(A)):
        A[i]-=B[i]
    return A

def replace(AA,B,k,m):
    j=0
    for i in range(k,m):
        AA[i]=B[j]
        j+=1

def sub2(AA,B):
    A = copy.copy(AA)
    for i in range(len(A[0])):
        A[0][i]-=B[0][i]
    return A