#!/usr/bin/env python3 

#-*-encoding:utf-8-*-



class Solution(object):
    def lengthOfLongestSubstring(self,s):
        """
        :type s: str
        :rtype: int
        """
        left,right=0,0
        maxCount=0
        d={}
        while right<len(s):
            if s[right] in d and d[s[right]]>=left:
                maxCount=maxCount if maxCount>=(right-left) else (right-left)
                left=d[s[right]]+1
            d[s[right]]=right
            right+=1
        maxCount=maxCount if maxCount>=(right-left) else (right-left)
        return maxCount



