#!/usr/bin/env python3 

#-*-coding:utf-8-*-

'''
define a listNode class , each node will have a next pointer which will point to next node
'''

class listNode(object):
    #When started to define a listNode, the next pointer refers to None
    def __init__(self,data):
        self._val=data
        self._next=None
    
    @property
    def val(self):
        return self._val
    
    @property
    def next(self):
        return self._next

    @val.setter
    def val(self,data):
        self._val=data

    @next.setter
    def next(self,data):
        self._next=data



listnode=listNode(1)
listnode.next=5
print(listnode.val)
print(listnode.next)












