#!/usr/bin/python

import unittest
'''
Follow up for Search in Rotated Sorted Array:

What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.

This is a linear solution
'''
def binarySearch_rotated(array, target):
         # write your code here
         start =0
         end = len(array)-1
         while start <= end:
               mid = (start+end)//2
               if array[mid] == target:
                  return True
               elif array[mid] > array[start]:
                  if target < array[mid] and target >= array[start]:
                       end =mid-1
                  else:
                      start =mid+1
               elif array[mid] < array[start]:
                  if target > array[mid] and target <= array[end]:
                     start =mid+1
                  else:
                     end =mid-1 
               else:
                    start+=1            
         return False

class Test(unittest.TestCase):
      data =[([1, 1, 0, 1, 1, 1],0,True),([1, 1, 1, 1, 1, 1],0,False)]

      def test_binarySearch(self):
          for test_data,target,expected in self.data:
              actual =binarySearch_rotated(test_data,target)
              self.assertEqual(actual,expected)

if __name__=="__main__":
    unittest.main()
