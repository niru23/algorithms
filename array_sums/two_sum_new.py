#!/usr/bin/python

import unittest

'''
Given an array A[] and a number x, check for pair in A[] with sum as x
Write a C program that, given an array A[] of n numbers and another number x, determines whether or not there exist two elements in S whose sum is exactly x. 
Basic method
sort the array and initialize two index left and right 
loop through
if A[i]+A[j] == x return 1
while i <j
elif A[i]+A[j] > x then j-1
elif A[i]+A[j] < x then i+1
'''

def 2sum(array,k):
    if len(array)< 2:
        return
    seen =set()
    output= set()
    for num in array:
        target =k-num
        if target in see:
           output.add(sort(num,target))
        else:
           seen.add(num)
     return output


class Test(unittest.TestCase):
      data =[([1,4,45,6,10,-8],16,True)]

      def test_get_two_sum(self):
          for test_data,target,expected in self.data:
              actual =two_sum(test_data,target)
              self.assertEqual(actual,expected)

if __name__=="__main__":
    unittest.main()


           
         
    

