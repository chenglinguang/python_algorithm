#!/usr/bin/env python3 

#-*-encoding:utf-8-*-

lst=[70,80,31,37,10,1,48,60,33,80]

def selection_sort(lst):
    for i in range(len(lst)-1): #只需要n-1(len(lst)-1)次即可
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

def updated_bubble_sort(lst):
    for i in range(len(lst)):
        found=False
        for j in range(1,len(lst)-i):
            if lst[j-1]>lst[j]:
                lst[j-1],lst[j]=lst[j],lst[j-1]
                found=True
        if found==False:
            return lst
    return lst


#print(updated_bubble_sort(lst))
def quick_sort(lst):
    qsort_rec(lst,0,len(lst)-1)
    
def qsort_rec(lst,a,b):
    if a>=b:
        return 
    i=a
    j=b
    pivot=lst[i]
    while i<j:
        while i<j and lst[j]>=pivot:
            j-=1
        if i<j:
            lst[i]=lst[j]
            i+=1
        while i<j and lst[i]<=pivot:
            i+=1
        if i<j:
            lst[j]=lst[i]
            j-=1
    lst[i]=pivot
    qsort_rec(lst,a,i-1)
    qsort_rec(lst,i+1,b)

#quick_sort(lst)
#print(lst)



    
    






