#!/usr/bin/python
import unittest
import time
'''
Time Complexity: O(n*n) as there are two nested loops.
Auxiliary Space: O(1)
The good thing about selection sort is it never makes more than O(n) swaps and can be useful when memory write is a costly operation.
'''
def selection_sort(a):
   n =len(a)
   for i in range(n):
       min_index =i
       for j in range(i+1,n):
           if a[min_index] >a[j]:
              min_index =j
       a[i],a[min_index] =a[min_index],a[i]
   return a 



class Test(unittest.TestCase):
      data =[([54, 26, 93, 17, 77, 31, 44, 55, 20],[17, 20, 26, 31, 44, 54, 55, 77, 93]),([2, 3, 2, 88, 3, 7, 10, 25, 1, 91],[1, 2, 2, 3, 3, 7, 10, 25, 88, 91])]
      
      def test_bubble_sort(self):
          for test_data,expected in self.data:
              actual =selection_sort(test_data)
              self.assertEqual(actual,expected) 
    
if __name__=="__main__":
    start_time = time.time()
    unittest.main()
    print("--- %s seconds ---" % (time.time() - start_time))
