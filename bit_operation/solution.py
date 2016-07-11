#!/usr/bin/env python3 

#-*-encoding:utf-8-*-

#思路：用位运算异或^,0与任何数异或结果为原数值，两个相同的数异或结果为0

def calc(ll):
    res=0
    for x in ll:
        res^=x
    return res


list1=[3,3,1,2,4,2,5,5,4]

print(calc(list1))


