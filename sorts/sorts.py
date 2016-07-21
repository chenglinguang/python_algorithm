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
#快速排序算法
def quick_sort(lst):
    qsort_rec(lst,0,len(lst)-1)

#递归函数    
def qsort_rec(lst,a,b):
    if a>=b:
        return                            #分段无记录或者只有一个记录
    i=a
    j=b
    pivot=lst[i]                          #初始空位
    while i<j:                            #寻找pivot的最终位置
        while i<j and lst[j]>=pivot:      
            j-=1                          #j向左扫描寻找小于pivot的记录
        if i<j:
            lst[i]=lst[j]
            i+=1                          #小记录移到左边
        while i<j and lst[i]<=pivot:       
            i+=1                          #i向右扫描找大于pivot的记录
        if i<j:
            lst[j]=lst[i]
            j-=1                          #大记录移动到右边
    lst[i]=pivot                          #讲pivot存入其最终位置
    qsort_rec(lst,a,i-1)                  #递归处理左半区
    qsort_rec(lst,i+1,b)                  #递归处理右半区

#quick_sort(lst)
#print(lst)



    
    






