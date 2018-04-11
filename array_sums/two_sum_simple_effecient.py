#!/usr/bin/python

import unittest

'''
Given an array A[] and a number x, check for pair in A[] with sum as x
Write a C program that, given an array A[] of n numbers and another number x, determines whether or not there exist two elements in S whose sum is exactly x. 
effecient method
 In this method use a dictionary.
create a dictionary with keys equal to the elements of an array and value is true if target -element exists in array
'''
def two_sum(array,target):
    n = len(array)
    hash_map = {}
    pairs_list=[]
    for i in range(n):
        if target-array[i] in hash_map:
           pairs =(target-array[i],array[i])
           if pairs not in pairs_list:
              pairs_list.append(pairs)
        else:
            hash_map[array[i]] =1
    return pairs_list    


class Test(unittest.TestCase):
      data =[([-1, 4, 45, 6, 10, 17],16,[(6, 10), (17, -1)])]

      def test_get_two_sum(self):
          for test_data,target,expected in self.data:
              actual =two_sum(test_data,target)
              self.assertEqual(actual,expected)

if __name__=="__main__":
    unittest.main()


           
         
    

