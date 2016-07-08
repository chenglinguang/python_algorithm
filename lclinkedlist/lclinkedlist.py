#!/usr/bin/env python3 

#-*-encoding-*-

class LCList() #循环单链表类
    def __init__(self):
        self._rear=None
    def is_empty(self):
        return self._rear is None
    def prepend(selfi,elem): #前段插入
        p=LNode(self)
        if self._rear is None:
            p.next=p #建立一个节点的环
            self._rear=p
        else:
            p.next=self._rear.next
            self._rear=p
    def append(self,elem): #后端插入
        self.prepend(elem)
        self._rear=self._rear.next
    def pop(self): #前段弹出
        if self._rear is None:
            raise LinkedListUnderflow('in pop of LCList')
        p=self._rear.next
        if self._rear is p:
            self.rear=None
        else:
            self._rear.next=p.next
        return p.elem
    def printall(self):#输出表元素
        if self.is_empty():
            return 
        p=self._rear.next
        while True:
            print(p.elem)
            if p is self._rear:
                break
            p=p.next




        

