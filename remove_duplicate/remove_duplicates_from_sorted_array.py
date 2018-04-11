#!/usr/bin/python

import unittest
'''
remove duplicates from sorted array  order of o(n)
'''
def remove_duplicates(array):
    if len(array)==0:
        return 0
    else:
         p1 =1
         p2 =1
         while p1 < len(array) and p2 < len(array):
               if array[p1]!=array[p1-1]:
                  array[p2] =array[p1]
                  p1+=1
                  p2+=1
               else:
                   p1+=1
         return p2

class Test(unittest.TestCase):
      data =[([1,1,2],2)]

      def test_binarySearch(self):
          for test_data,expected in self.data:
              actual =remove_duplicates(test_data)
              self.assertEqual(actual,expected)
if __name__=="__main__":
    unittest.main()
