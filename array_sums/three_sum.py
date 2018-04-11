#!/usr/bin/python

import unittest

'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
For example, given array S = {-1 0 1 2 -1 -4}, A solution set is:
(-1, 0, 1)
(-1, -1, 2)
sort the array and perform the same procedure as two sum
'''
def three_sum(array,target):
    array.sort()
    triplets =[]
    for i in range(len(array)-2):
        start =i+1
        end =len(array)-1
        while start < end:
              if array[i]+array[start]+array[end] ==target:
                triplets.append([array[i],array[start],array[end]])
                start+=1
                end-=1
              elif array[i]+array[start]+array[end] < target:
                 start+=1
              else:
                 end-=1
    return triplets    
                     

class Test(unittest.TestCase):
      data =[([-1, 0, 1, 2, -1, -4],0,[[-1, -1, 2], [-1, 0, 1], [-1, 0, 1]])]

      def test_get_two_sum(self):
          for test_data,target,expected in self.data:
              actual =three_sum(test_data,target)
              self.assertEqual(actual,expected)

if __name__=="__main__":
    unittest.main()


           
         
    

