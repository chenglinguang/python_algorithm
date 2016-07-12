#!/usr/bin/env python3 

#-*-encoding:utf-8-*-

list1=[7, -8, 5, 4, 0, -2, -5]
#1.正数在前负数在后 2.整数从小到大 3.负数从大到小


#两步排序
list2=sorted(list1,key=lambda x:(x<0,abs(x)))
list3=sorted(list1,key=lambda x:(x<0,x if x>=0 else -x))

print(list2)
print(list3)
