#!/usr/bin/env python3 

#-*-encoding:utf-8-*-

#解题思路：
#一个表中两个片段，左边是已经排列好的，右边是没排列好的
#从右边第一个没排列好的元素开始与左边依此比较，然后进行插入操作

def list_sort(lst):
    #先排好[0:1]片段
    if lst[0]>lst[1]:
        tmp=lst[0]
        lst[0]=lst[1]
        lst[1]=tmp
    for i in range(1，len(lst))：
        x=lst[i]
        j=i
        while j >0 and lst[j-1]>x:
            lst[j]=lst[j-1]
            j-=1
        lst[j]=x



