#!/usr/bin/env python3 

#-*-encoding:utf-8-*-

def josephus_list(n,k,m):

    #建立一个n个人的表
    people=list(range(1,n+1))
    #i表示数组下标
    i=k-1
    #大循环一次迭代出列一人，共计执行n次迭代
    for num in range(n):
        #count用于计数直到m，
        count=0
        while count<m:
            if people[i]>0:
                count+=1
            if count==m:
                print(people[i]," get=out")
                people[i]=0
            i=(i+1)%n

    return

josephus_list(10,2,7)

         
