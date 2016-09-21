#!/usr/bin/env python3 

#-*-encoding:utf-8-*-

#[1]
#[1,1]
#[1,2,1]
#[1,3,3,1]

def getTriangle(n):
    N=[1]
    if n==1:
        print(N)
    while(n-1):
        N.append(0)
        N=[N[i-1]+N[i] for i in range(len(N))]
        print(N)
        n=n-1
         
if __name__=="__main__":
    getTriangle(5)

 
