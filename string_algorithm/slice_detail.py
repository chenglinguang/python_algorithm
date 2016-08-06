#!/usr/bin/env python3 

#-*-encoding:utf-8-*-

#realize the [a,b,k] slice

str1='abcdefghijk'

def slice_sub(s,a,b,k):
    newstr=''
    for i in range(a,b,k):
        newstr+=s[i]
    return newstr

print(slice_sub(str1,0,6,2))


