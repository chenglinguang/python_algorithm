#!/usr/bin/env python3 

#-*-encoding:utf-8-*-

def naive_matching(t,p):
    m,n=len(p),len(t)
    i,j=0,0
    while i<m and j<n:
        if p[i]==t[j]:
            i,j=i+1,j+1
        else:
            i,j=0,j-i+1
    if i==m:
        return j-i
    else:
        return 

str1='abcdefghijklmn'
substr='fgh'

print(naive_matching(str1,substr))


        
