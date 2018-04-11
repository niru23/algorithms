#!/usr/bin/python
import unittest
import time
'''
'''
def merge_sort(a):
   if len(a) <=1:
      return a
   mid =len(a)//2
   left = merge_sort(a[:mid])
   right = merge_sort(a[mid:])
   return merge(left,right)

def merge(l,r):
   if not l :
      return r
   if not r:
      return l
   if l[0] <r[0]:
      return [l[0]]+merge(l[1:],r)
   return [r[0]]+merge(l,r[1:]) 
 

class Test(unittest.TestCase):
      data =[([54, 26, 93, 17, 77, 31, 44, 55, 20],[17, 20, 26, 31, 44, 54, 55, 77, 93]),([2, 3, 2, 88, 3, 7, 10, 25, 1, 91],[1, 2, 2, 3, 3, 7, 10, 25, 88, 91])]
      
      def test_merge_sort(self):
          for test_data,expected in self.data:
              actual =merge_sort(test_data)
              self.assertEqual(actual,expected) 
    
if __name__=="__main__":
    start_time = time.time()
    unittest.main()
    print("--- %s seconds ---" % (time.time() - start_time))
