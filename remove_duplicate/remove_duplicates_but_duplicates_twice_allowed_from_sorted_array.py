#!/usr/bin/python

import unittest
'''
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array A = [1,1,1,2,2,3],

Your function should return length = 5, and A is now [1,1,2,2,3].
'''
def remove_duplicates(array):
    if len(array)==0:
        return 0
    else:
         curr =2
         prev =1
         while curr < len(array) and prev < len(array):
                if array[curr] ==array[prev] and array[curr]==array[prev-1]:
                   curr+=1
                else:
                    prev+=1
                    array[prev]=array[curr]
                    curr+=1
    
         return prev+1

class Test(unittest.TestCase):
      data =[([1,1,1,1,2,2,2,3,3,3],6)]

      def test_binarySearch(self):
          for test_data,expected in self.data:
              actual =remove_duplicates(test_data)
              self.assertEqual(actual,expected)
if __name__=="__main__":
    unittest.main()
