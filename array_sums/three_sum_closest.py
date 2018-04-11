#!/usr/bin/python

import unittest
import sys
'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers.
For example, given array S = [-1 2 1 -4], and target = 1. The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
sort the array and perform the same procedure as two sum
'''
def three_sum_close(array,target):
    array.sort()
    result =0
    diff =sys.maxint 
    for i in range(len(array)-2):
        start =i+1
        end =len(array)-1
        while start < end:
              sum = array[i]+array[start]+array[end]
              if diff >abs(target-sum):
                 diff = abs(target-sum)
                 result = sum
              if sum == target:
                 return sum
              elif array[i]+array[start]+array[end] < target:
                 start+=1
              else:
                 end-=1
    return result    
                     

class Test(unittest.TestCase):
      data =[([-1, 2, 1, -4],1,2)]

      def test_three_sum_close(self):
          for test_data,target,expected in self.data:
              actual =three_sum_close(test_data,target)
              self.assertEqual(actual,expected)

if __name__=="__main__":
    unittest.main()


           
         
    

