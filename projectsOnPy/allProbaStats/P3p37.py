# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 16:24:31 2021

@author: luiso
"""
def Ehiper(n, M, N):
    return n*M/N

def Vhiper(n, M, N):
    return (N-n)/(N-1)*n*M/N*(1-M/N)

n=10
M=5
N=25

R1=Ehiper(n, M, N)
R2=Vhiper(n, M, N)


print(R1)
print(R2)