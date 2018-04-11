#!/usr/bin/python

import unittest
'''
Binary search order of log(n)
'''
def recover_rotated_array(array):
         n =len(array)
         index =0
         while index <n:
               if array[index] <array[index-1]:
                  break
               else:
                   index+=1
         reverse_array(array,0,index-1)
         reverse_array(array,index,n-1)
         reverse_array(array,0,n-1)
         return array

def reverse_array(array,start,end):
        while start < end:
           temp =array[start]
           array[start] =array[end]
           array[end] =temp
           start+=1
           end-=1

class Test(unittest.TestCase):
      data =[([4, 5, 1, 2, 3],[1, 2, 3, 4, 5])]

      def test_recover_rotated_array(self):
          for test_data,expected in self.data:
              actual =recover_rotated_array(test_data)
              self.assertEqual(actual,expected)

if __name__=="__main__":
    unittest.main()
