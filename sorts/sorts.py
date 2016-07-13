#!/usr/bin/env python3 

#-*-encoding:utf-8-*-

lst=[70,80,31,37,10,1,48,60,33,80]

def selection_sort(lst):
    for i in range(len(lst)):
        min_index=i
        for j in range(i,len(lst)):
            if lst[min_index]>lst[j]:
                min_index=j
        lst[i],lst[min_index]=lst[min_index],lst[i]
    return lst

def insert_sort(lst):
    for i in range(1,len(lst)): #第一位不用再排序
        j=i
        tmp=lst[i]
        while j>0 and lst[j-1]>tmp:
            lst[j]=lst[j-1]
            j=j-1
        lst[j]=tmp
    return lst

def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(1,len(lst)-i):
            if lst[j-1] >lst[j]:
                lst[j-1],lst[j]=lst[j],lst[j-1]
    return lst

        

print(bubble_sort(lst))






