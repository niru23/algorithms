#!/usr/bin/python

import unittest
'''
insertion sort order of log(n)
'''
def insertion_sort(array):
    for i in range(1,len(array)):
         for j in range(i-1,-1,-1):
             if A[j] >A[j+1]:
                A[j],A[j+1] =A[j+1],A[j]
             else:
                break
    return array 

     
class Test(unittest.TestCase):
      data =[([54, 26, 93, 17, 77, 31, 44, 55, 20],[17, 20, 26, 31, 44, 54, 55, 77, 93])]

      def insertion_sort(self):
          for test_data,expected in self.data:
              actual =insertion_sort(test_data,target)
              self.assertEqual(actual,expected)

if __name__=="__main__":
    unittest.main()
