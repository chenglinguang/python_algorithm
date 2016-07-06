#!/usr/bin/env python3 

#!-*-encoding-*-

#定义一个基于节点类的单链表对象类

class LNode:
    #_next防止与python标准函数next重名
    def __init__(self,elem,_next=None):
        self.elem=elem
        self.next=_next

class LList:
    def __init__(self):
         #初始化为None表示建立的为空表
         self._head=None
    
    def is_empty(self):
         return self._head is None
    
    #表头插入数据
    def prepend(self,elem):
        self._head=LNode(elem,self._head)
    
    #删除表头节点并返回节点里边的数据
    def pop(self):
        if self._head is None: #无节点引发异常
            raise LinkedListUnderflow('in pop')
        e=self._head.elem
        self._head=self.head.next
        return e
    #后端操作，后端加入
    def append(self,elem):
        if self._head is None:
            self._head=LNode(elem)
            return
        p=self._head
        while p.next is not None:
            p=p.next
        p.next=LNode(elem)




