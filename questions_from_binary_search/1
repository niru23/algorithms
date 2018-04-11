#!/usr/bin/python

import unittest
'''
Watson gives Sherlock an array A of length N. Then he asks him to determine if there exists an element in the array such that the sum of the elements on its left is equal to the sum of the elements on its right. If there are no elements to the left/right, then the sum is considered to be zero.
Formally, find an i, such that, A1+A2= A5+A6  and A3 partitions
If the target number does not exist in the array, return -1.
'''
def sherlock_array(array):
        # write your code here
        left = 0
        right = len(array)-1
        left_sum =0
        right_sum =0
        while left != right:
              if left_sum <= right_sum:
                 left+=1
                 left_sum+=array[left]
              else:
                 right-=1
                 right_sum+=array[right]
        if left_sum == right_sum:
          return 'YES'
        else:
          return 'NO'

class Test(unittest.TestCase):
      data =[([1, 2, 3, 3],'YES'),([1, 2, 3],'NO')]

      def test_sherlock_array(self):
          for test_data,expected in self.data:
              actual =sherlock_array(test_data)
              self.assertEqual(actual,expected)

if __name__=="__main__":
    unittest.main()
