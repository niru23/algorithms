#!/usr/bin/python

import unittest
'''
There is an integer array which has the following features:

The numbers in adjacent positions are different.
A[0] < A[1] && A[A.length - 2] > A[A.length - 1].
We define a position P is a peek if:
A[P] > A[P-1] && A[P] > A[P+1]
The array may contains multiple peeks, find any of them.
'''
def findPeak(nums):
        # write your code here
        start =0
        end =len(nums)-1
        while start < end :
            mid =(start+end)//2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
               return mid
            elif nums[mid] < nums[mid+1]:
               start =mid+1
            else:
               end = mid-1
        return start


class Test(unittest.TestCase):
      data =[([1, 2, 1, 3, 4, 5, 7, 6],6)]

      def test_binarySearch(self):
          for test_data,expected in self.data:
              actual =findPeak(test_data)
              self.assertEqual(actual,expected)

if __name__=="__main__":
    unittest.main()
