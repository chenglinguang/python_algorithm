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

#归并排序算法
#把两个或者更多有序序列归并成为一个有序序列

#merge(lfrom,lto,low,mid,high)实现对列表中连续排放的两个有序序列的归并工作。
#注意是连续排放，并且是有序序列，归并到另外的列表中形成一个列表。
#两个连续序列为：low--mid-1 , mid--high-1
def merge(lfrom,lto,low,mid,high):
    i,j,k=low,mid,low
    while i <mid and j <high : #反复复制两个分段中最小的
        if lfrom[i]<=lfrom[j]:
            lto[k]=lfrom[i]
            i+=1
        else:
            lto[k]=lfrom[j]
            j=j+1
        k+=1
    while i<mid:
        lto[k]=lfrom[i]
        i+=1
        k+=1
    while j<high:
        lto[k]=lfrom[j]
        j+=1
        k+=1

#merge_pass实现一对对分段的一遍归并，它需要知道表长度（llen）和分段长度（slen）

def merge_pass(lfrom,lto,llen,slen):
    i=0
    #处理一对对长度为slen的分段
    while i+2*slen<llen:    #归并长slen的两断
        merge(lfrom,lto,i,i+slen,i+2*slen)
        i+=2*slen
    if i+slen < llen: #剩下两断，后段长度小于slen
        merge(lfrom,lto,i,i+slen,llen)
    else:             #只剩下一段，复制到表lto中
        for j in range(i,llen):
            lto[j]=lfrom[j]

#先安排一个同样长度的表，然后在两个表中往复一遍遍的做归并操作
#整个归并完成是可能正好存放在结果templst中，这个时候再做一次merge_pass（循环中第二个merge_pass调用），就能把结果复制回原来的列表lst
def merge_sort(lst):
    slen,llen=1,len(lst)
    templst=[None]*llen
    while slen<llen:
        merge_pass(lst,templst,llen,slen)
        slen*=2
        merge_pass(templst,lst,llen,slen)
        slen*=2























    
    






