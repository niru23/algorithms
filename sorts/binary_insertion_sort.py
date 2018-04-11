#!/usr/bin/python

import unittest
'''
Boundary Cases: Insertion sort takes maximum time to sort if elements are sorted in reverse order. 
And it takes minimum time (Order of n) when elements are already sorted.
Algorithmic Paradigm: Incremental Approach
Sorting In Place: Yes
Stable: Yes
Online: Yes
Uses: Insertion sort is uses when number of elements is small. 
It can also be useful when input array is almost sorted, only few elements are misplaced in complete big array.
'''

def binary_search(a,target,start,end):
    while start <=end:
          mid =(start+end)//2
          if a[mid] ==target:
             return mid+1
          elif a[mid] > target:
               end = mid-1
          else:
               start =mid+1

def binary_insertion_sort(a):
    n = len(a)
    for i in range(1,n):
        j =i-1
        key =a[i]
        loc = binary_search(a,target,0,j)
        while j >=loc:
              a[j+1] =a[j]
              j-=1
        a[j+1] =key
    return a

def insertion_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(i-1,-1,-1):
            if a[j] >a[j+1]:
               a[j],a[j+1] =a[j+1],a[j]
            else:
                break
    return array

class Test(unittest.TestCase):
      data =[([54, 26, 93, 17, 77, 31, 44, 55, 20],[17, 20, 26, 31, 44, 54, 55, 77, 93])]

      def insertion_sort(self):
          for test_data,expected in self.data:
              actual =binary_insertion_sort(test_data,target)
              self.assertEqual(actual,expected)

if __name__=="__main__":
    unittest.main()
