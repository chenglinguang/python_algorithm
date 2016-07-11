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
    llist.reverse()
    return llist




                 
print(get_reverse_1(l1))
print(get_reverse_2(l1))



 
