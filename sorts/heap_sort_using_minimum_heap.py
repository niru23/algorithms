#!/usr/bin/python
import unittest
'''
simple heap sort using minimum heap
'''
def heapify(array,start,end):
    smallest =start
    left = 2*start+1
    right = 2*start+2
    if left < end and array[left] <array[smallest]:
       smallest = left
    if right < end and array[right] < array[smallest]:
       smallest =right
    if start != smallest:
       array[start],array[smallest] = array[smallest],array[start]
       heapify(array,smallest,end)

def heap_sort(array):
    l = len(heap_sort)
    for i in range(l,-1-1):
        heapify(array,i,l)
    for i in range(l,0,-1):
        array[i],array[0] =array[0],array[i]
        heapify(array,0,i)
    return array


        
class Test(unittest.TestCase):
      data =[([54, 26, 93, 17, 77, 31, 44, 55, 20],[17, 20, 26, 31, 44, 54, 55, 77, 93])]

      def heap_sort(self):
          for test_data,expected in self.data:
              actual =heap_sort(test_data)
              self.assertEqual(actual,expected)

if __name__=="__main__":
    unittest.main()




