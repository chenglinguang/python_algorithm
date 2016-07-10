#!/usr/bin/env python3 

#-*-encoding:utf-8-*-

def josephuse_L(n,k,m):
    people=list(range(1,n+1))
    
    num,i=n,k-1
    #num表示表长度，每退出一个人，num自动减一
    for num in range(n,0,-1):
        #从i开始数，数m个
        i=(i+m-1)%num
        print(people.pop(i))
    return


josephuse_L(10,2,7)
        
        
