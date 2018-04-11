#!/usr/bin/python

import unittest
'''
For a given sorted array (ascending order) and a target number, find the first index of this number in O(log n) time complexity.

If the target number does not exist in the array, return -1.
'''
def binarySearch(nums, target):
        # write your code here
        first =0
        last = len(nums) -1
        while first <= last:
            if target == nums[first]:
                return first
            else:
                     first = first+1
        return -1 

class Test(unittest.TestCase):
      data =[([1, 2, 3, 3, 4, 5, 10],3,2)]

      def test_binarySearch(self):
          for test_data,target,expected in self.data:
              actual =binarySearch(test_data,target)
              self.assertEqual(actual,expected)

if __name__=="__main__":
    unittest.main()
