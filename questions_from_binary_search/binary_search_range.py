#!/usr/bin/python

import unittest
'''
Given a sorted array of n integers, find the starting and ending position of a given target value.

If the target is not found in the array, return [-1, -1]
This is a modification to binary search where you do not return when an element is found instead you find the first occurance by setting end = mid-1 and 
last occurance by seeting start = mid+1
'''
def binarySearch_getRange(A, target):
        # write your code here
        if not A:
            return [-1,-1]
        if len(A)==1:
            return [0,0]
        # get the first occurance
        start = 0
        end = len(A)-1
        index =-1
        index_list =[-1,-1]
        while start <= end:
            mid = (start+end)//2
            if target == A[mid] :
                index= mid
                end = mid-1
            elif target < A[mid]:
                 end = mid-1
            else:
                 start =mid+1
         
        if index==-1:
           return index_list
        else:
            index_list[0] = index
            # get the last occurance
            start =0
            end =len(A)-1
            while start <= end:
                mid = (start+end)//2
                if target == A[mid] :
                    index= mid
                    start = mid+1
                elif target < A[mid]:
                    end = mid-1
                else:
                     start =mid+1
            index_list[1]=index
            return index_list

class Test(unittest.TestCase):
      data =[([5,5,5,5,5,5,5,5,5,5],5,[0,9])]

      def test_binarySearch_getRange(self):
          for test_data,target,expected in self.data:
              actual =binarySearch_getRange(test_data,target)
              self.assertEqual(actual,expected)

if __name__=="__main__":
    unittest.main()
