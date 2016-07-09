#!/usr/bin/env python3 

#!-*-encoding:utf-8-*-

#定义一个基于节点类的单链表对象类

class LNode:
    __slots__=['elem','next']
    #_next防止与python标准函数next重名
    def __init__(self,elem,_next=None):
        self.elem=elem
        self.next=_next
    def getElem(self):
        return self.elem
    def getNext(self):
        return self.next
    def setElem(self,newelem):
        self.elem=newelem
    def setNext(self,newnext):
        self.next=newnext


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
    #取得链表的长度
    def size(self):
        p=self._head
        count=0
        while p is not None:
            count+=1
            p=p.next
        return count
    #后端操作，后端加入
    def append(self,elem):
        if self._head is None:
            self._head=LNode(elem)
            return
        p=self._head
        while p.next is not None:
            p=p.next
        p.next=LNode(elem)

    #删除最后一个元素
    def pop_last(self):
        #如果链表为空表
        if self._head is None:
            raise LinkedListUnderflow('in pop_last')
        
        #如果链表只有一个元素
        p=self._head
        if p.next is None:
            e=p.elem
            self._head=None
            return e
        
        while p.next.next is not None: #直到p.next是最后一个元素
            p=p.next
        e=p.next.elem
        p.next=none
        return p

    def find(self,pred):
        p=self._head
        while p is not None:
            if pred(p.elem):
                return p.elem
            p=p.next

    #打印所有的节点元素
    def print_all(self):
        p=self._head
        while p is not None:
            print(p.elem)
            print('end')
            p=p.next
    #检索元素是否在链表中
    def search_of(self,item):
        p=self._head
        while p is not None:
            if p.elem==item:
                return 1
            p=p.next
        return 0
     #index , 元素在链表中的位置：
    def index_of(self,item):
        p=self._head
        count=0
        while p is not None:
            if p.elem==item:
                return count
            else:
                p=p.next
            count+=1
        raise ValueError('%s is not in linkedlist'%item)
    
    #删除链表中的某元素
    def remove(self,item):
        p=self._head
        pre=None
        while p is not None:
            if p.elem==item:
                #如果是第一个元素
                if not pre:
                    self._head=p.next
                else:
                    pre.next=p.next
                break
            else:
                pre=p
                p=p.next 
    #insert链表中插入元素
    def insert(self,pos,item):
       if pos<=1:
           self.prepend(item)
       elif pos>self.size():
           self.append(item)
       else:
           temp=LNode(item)
           count=1
           pre=None
           p=self._head
           while count<pos:
               count=count+1
               pre=p
               p=p.next
           pre.next=temp
           temp.next=p 

    #定义一个生成器函数yield，使链表对象成为迭代器
    #for x in llist1.elements():
    #    print(x)
    def elements(self):
        p=self._head
        while p is not None:
            yield p.elem
            p=p.next

    #筛选生成器
    def filter(self,pred):
        p=self._head
        while p is not None:
            if pred(p.elem):
                yield p.elem
            p=p.next
    #反转单链表
    def rev(self):
        p=None
        while self._head is not None:
            cur=self._head
            self._head=self._head.next
            cur.next=p
            p=cur
        self._head=p

mlist1=LList()
for i in range(1,10):
    mlist1.prepend(i)
for i in range(11,20):
    mlist1.append(i)
mlist1.print_all()
print(mlist1.search_of(10))

















 




