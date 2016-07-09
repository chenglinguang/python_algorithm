#!/usr/bin/env python3 

#-*-encoding:utf-8-*-


from listnode import LNode 
from lclinkedlist import LCList
class DLNode(LNode):
    def __init__(self,elem,prev=None,_next=None):
        LNode.__init__(self,elem,_next)
        self.prev=prev

#双链表类
class DLList(LList):
    def __init__(self):
        LList.__init__(self)
    def prepend(self,elem):
        p=DLNode(elem,None,self._head)
        if self._head is None: #空表
            self._rear=p
        else:
            p.next.pre=p
        self._head==p
    def pop(self):
        if self._head is None:
            raise LinkedListUnderFlow('in pop of DLList')
        e=self._head.elem
        self._head=self._head.next
        if self._head is not None:
            self._head.prev=None
        return e
    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderFlow('in pop of DLList')
        e=self._rear.elem
        self._rear=self._rear.prev
        if self._rear is None:
            self._head=None
        else:
            self._rear.next=None
        return e





  
    




