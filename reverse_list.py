#!/usr/bin/env python3 

#-*-coding:utf-8-*-

l1=['A','B','C']


def get_reverse_1(llist):
    new=[]
    if llist:
        length=len(llist)
        for i in range(length):
            new.append(llist[length-i-1])
        return new
 
def get_reverse_2(llist):
    #llist.reverse()
    #return llist
    new=list(reversed(llist))
    return new

def get_reverse_3(llist):
    new=llist[::-1]
    return new

def get_reverse_4(llist):
    length=len(llist)
    half=length//2
    if half==0:
        return llist
    for i in range(half):
        llist[i],llist[length-i-1]=llist[length-i-1],llist[i]
    return llist

            

                 
print(get_reverse_1(l1))
print(get_reverse_2(l1))
print(get_reverse_3(l1))
print(get_reverse_4(l1))


 
