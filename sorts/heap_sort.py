#!/usr/bin/python
import unittest
def heapify(array,start,end):
    largest =start
    left =2*start+1
    right =2*start+2
    if left < end and array[left] >array[largest]:
       largest =left
    if right < end and array[right] > array[largest]:
       largest =right
    if start != largest:
       array[start],array[largest] =array[largest],array[start]
       heapify(array,largest,end)

def heap_sort(array):
    l =len(array)
    # heapify from bottom
    for i in range(l,-1,-1):
        heapify(array,i,l)
    # now the max element is on the top.
    # replace it with last element and reduce the size of the array
    for i in range(l-1,0,-1):
        array[i],array[0] =array[0],array[i]
        heapify(array,0,i) 
    return array
          
class Test(unittest.TestCase):
      data =[([54, 26, 93, 17, 77, 31, 44, 55, 20],[17, 20, 26, 31, 44, 54, 55, 77, 93]),([2, 3, 2, 88, 3, 7, 10, 25, 1, 91],[1, 2, 2, 3, 3, 7, 10, 25, 88, 91])]

      def heap_sort(self):
          for test_data,expected in self.data:
              actual =heap_sort(test_data)
              self.assertEqual(actual,expected)
    
if __name__=="__main__":
    unittest.main()


