#!/usr/bin/python
import unittest
'''
Given two array of integers(the first array is array A, the second array is array B), now we are going to find a element in array A which is A[i], and another element in array B which is B[j], so that the difference between A[i] and B[j] (|A[i] - B[j]|) is as small as possible, return their smallest difference.

For example, given array A = [3,6,7,4], B = [2,8,9,3], return 0
'''



import sys
class Solution:
    # @param A, B: Two lists of integer
    # @return: An integer
 
    def smallestDifference(self, A, B):
        # write your code here
        if len(A)==1 and len(B)==1:
            return abs(A[0]-B[0])
        A.sort()
        B.sort()
        i =0
        j =0
        curr_len =0
        min_length =abs(A[0]-B[0])
        while i< len(A) and j <len(B):
                min_length =min(min_length,abs(A[i]-B[j]))
                if A[i] < B[j]:
                  i+=1
                else:
                   j+=1
        return  min_length 
