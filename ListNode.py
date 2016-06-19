#!/usr/bin/env python3 

#-*-coding:utf-8-*-

'''
define a listNode class , each node will have a next pointer which will point to next node
'''

class listNode(object):
    #When started to define a listNode, the next pointer refers to None
    def __init__(self,data):
        self.val=data
        self.next=None
    
    @property
    def val(self):
        return self.val
    
    @property
    def next(self):
        return self.next

    @val.setter
    def val(self,data):
        self.val=data

    @next.setter
    def next(self,data):
        self.next=data
