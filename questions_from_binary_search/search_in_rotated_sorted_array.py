#!/usr/bin/python

import unittest
'''
Search in Rotated Sorted Array
Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
'''
def binarySearch_rotated(array, target):
         # write your code here
         start =0
         end = len(array)-1
         while start <= end:
               mid = (start+end)//2
               if array[mid] == target:
                  return mid
               if array[mid] >=array[start]:
                  if target < array[mid] and target >= array[start]:
                       end =mid-1
                  else:
                      start =mid+1
               if array[mid] < array[end]:
                  if target > array[mid] and target <= array[end]:
                     start =mid+1
                  else:
                     end =mid-1       
         return -1

class Test(unittest.TestCase):
      data =[([4, 5, 1, 2, 3],1,2),([4, 5, 1, 2, 3],0,-1)]

      def test_binarySearch(self):
          for test_data,target,expected in self.data:
              actual =binarySearch_rotated(test_data,target)
              self.assertEqual(actual,expected)

if __name__=="__main__":
    unittest.main()
