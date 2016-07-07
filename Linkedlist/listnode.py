#!/usr/bin/env python3 

#!-*-encoding:utf-8-*-

#定义一个节点类与应用
class LNode:
    def __init__(self,elem,_next=None):
        self.elem=elem
        #_next避免与python标准函数重名
        self.next=_next
    
llist1=LNode(1)
p=llist1

for i in range(2,11):
    p.next=LNode(i)
    p=p.next

#相当于p又指向了head
p=llist1
while p is not None:
    print(p.elem)
    p=p.next


    
    
