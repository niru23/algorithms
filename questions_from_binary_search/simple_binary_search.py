#!/usr/bin/python

import unittest
'''
Binary search order of log(n)
'''
def binarySearch(array, target):
         # write your code here
         start =0
         end = len(array)-1
         while start <= end:
               mid = (start+end)//2
               if array[mid] == target:
                  return True
               elif array[mid] < target:
                    start = mid+1
               else:
                    end = mid-1
         return False

class Test(unittest.TestCase):
      data =[([0, 1, 2, 8, 13, 17, 19, 32, 42],32,True),([0, 1, 2, 8, 13, 17, 19, 32, 42],342,False),([0, 1, 2, 8, 13, 17, 19, 32, 42],0,True)]

      def test_binarySearch(self):
          for test_data,target,expected in self.data:
              actual =binarySearch(test_data,target)
              self.assertEqual(actual,expected)

if __name__=="__main__":
    unittest.main()
