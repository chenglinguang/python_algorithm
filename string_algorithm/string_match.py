#!/usr/bin/env python3 

#-*-encoding:utf-8-*-

def naive_matching(t,p):
    m,n=len(p),len(t)
    i,j=0,0
    while i <m and j <n:      #i==m说明找到匹配
        if p[i]==t[j]:        #字符相同考虑下一对字符
            i,j=i+1,j+1
        else:                 #字符不同考虑t中下一个字符
            i,j=0,j-i+1
    if i==m:            #找到匹配，返回下标
        return j-i
    else:
        return -1



