#!/usr/bin/python
import unittest
import time
'''
Bubble sort 
Best case order of n
worst case order of (n*n)
best case when array is already sorted
Boundary cases Bubble sort takes minimum time (Order of n) when elements are already sorted.
sorting is in place 
stable yes
'''
def bubble_sort(a):
   n =len(a)
   for i in range(n):
       for j in range(0,n-i-1):
           if a[j] > a[j+1]:
              a[j],a[j+1]=a[j+1],a[j]
   return a 


def optimized_bubble_sort(a):
    n = len(a)
    
    for i in range(n):
       swapped = False
       for j in range(0,n-i-1):
           if a[j] > a[j+1]:
              a[j],a[j+1]=a[j+1],a[j]
              swapped = True
       if not swapped:
              break  
    return a

class Test(unittest.TestCase):
      data =[([54, 26, 93, 17, 77, 31, 44, 55, 20],[17, 20, 26, 31, 44, 54, 55, 77, 93]),([2, 3, 2, 88, 3, 7, 10, 25, 1, 91],[1, 2, 2, 3, 3, 7, 10, 25, 88, 91])]
      
      def test_bubble_sort(self):
          for test_data,expected in self.data:
              actual =bubble_sort(test_data)
              self.assertEqual(actual,expected) 
      def test_optimized_bubble_sort(self):
          for test_data,expected in self.data:
              actual =optimized_bubble_sort(test_data)
              self.assertEqual(actual,expected)    
    
if __name__=="__main__":
    start_time = time.time()
    unittest.main()
    print("--- %s seconds ---" % (time.time() - start_time))
