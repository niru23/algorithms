#!/usr/bin/python
import unittest
'''
   Partition Array:- Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:
   All elements < k are moved to the left
   All elements >= k are moved to the right
   Return the partitioning index, i.e the first index i nums[i] >= k.
   You should do really partition in array nums instead of just counting the numbers of integers smaller than k.
'''
def partitionArray(nums, k):
        # write your code here
        # you should partition the nums by k
        # and return the partition index as description
        if not nums:
           return 0
        right =len(nums)-1
        left = 0
        done = False
        while not done:
            while left <= right and nums[left] <k:
                  left+=1
            while right >= left and nums[right] >=k:
                  right-=1
            if  right < left:
                done = True
            else:
                temp = nums[left]
                nums[left] =nums[right]
                nums[right]=temp
        return right+1

class Test(unittest.TestCase):
      data =[([7,7,9,8,6,6,8,7,9,8,6,6],10,12)]

      def insertion_sort(self):
          for test_data,test_pivot,expected in self.data:
              actual =partitionArray(test_data,target)
              self.assertEqual(actual,expected)

if __name__=="__main__":
    unittest.main()


