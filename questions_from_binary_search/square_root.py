#!/usr/bin/python

import unittest
'''
square root  of a number using binary search
If the target number does not exist in the array, return -1.
'''
def square_root(num):
        # write your code here
        start =1
        end =(num/2)+1
        while start <= end:
             central = (start+end)//2
             if central**2 ==num:
                return central
             elif central**2 > num:
                  end =central-1
             else :
                  start= central+1
        return end  

class Test(unittest.TestCase):
      data =[(3,1),(4,2),(5,2),(10,3)]

      def test_square_root(self):
          for test_data,expected in self.data:
              actual =square_root(test_data)
              self.assertEqual(actual,expected)

if __name__=="__main__":
    unittest.main()
