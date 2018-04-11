#!/usr/bin/python

import unittest
'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

 Notice

You may assume no duplicate exists in the array.
'''
def findMin(nums):
        # write your code here
        start =0
        end =len(nums)-1
        while start < end and nums[start] >nums[end]:
            mid =(start+end)//2
            if nums[mid] < nums[end]:
               end =mid
            else:
                start =mid+1
        return nums[start]


class Test(unittest.TestCase):
      data =[([4, 5, 6, 7, 0, 1, 2],0)]

      def test_binarySearch(self):
          for test_data,expected in self.data:
              actual =findMin(test_data)
              self.assertEqual(actual,expected)

if __name__=="__main__":
    unittest.main()
