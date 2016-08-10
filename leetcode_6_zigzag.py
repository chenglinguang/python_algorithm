#!/usr/bin/env python3 

#-*-encoding:utf-8-*-
'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

find the solution:
第一行与最后一行：step=2*numRows-2
其他行：2*numRows-2 为最大的列
下一小列与最大列之间的关系为：2*n-2*i-2或者step-2*i
'''

class Solution(object):
    def convert(self,s,numRows):
        if numRows==1:
            return s
        step=2*numRows+2
        #the first row 
        ret=s[::step]
        #1到numRows-1行
        for i in range(1,numRow-1):
            for j in range(i,len(s),step):
                ret+=s[j]
                if j+(2*n-2*i-2)<len(s):
                    ret+=s[j+2*n-2i-2]
        #last row
        ret+=s[numRows-1::step]
        return ret


            











