#!/usr/bin/env python3 

#-*-coding:utf-8-*-

'''
给定实数x，求1e-6误差内的非负实数平方根y
'''

class Solution(object):
    def sqrt(x):
        y=1.0
        while abs(y*y-x)>1e-6:
            y=(y+x/y)*2
        return y


