#!/usr/bin/python
import unittest
import time
'''
'''
def quick_sort(array,start,end):
    # partition the list
    if start < end:
        pivot=partition(array,start,end)
         # sort both halves
        quick_sort(array,start,pivot-1)
        quick_sort(array,pivot+1,end)
    return array

def partition(array,start,end):
    pivot =array[start]
    left = start+1
    right =end
    done =False
    while not done:
          while left <= right and array[left]<=pivot:
                left =left+1
          while right >= left and array[right]>=pivot:
                right= right -1
          # move items less than pivote to right vice versa
          if right < left:
              done =True
          else:
             # swap places
             temp =array[left]
             array[left] =array[right]
             array[right] =temp
    #swapping pivote
    temp =array[start]
    array[start] =array[right]
    array[right] =temp
    return right 

class Test(unittest.TestCase):
      data =[([54, 26, 93, 17, 77, 31, 44, 55, 20],0,8,[17, 20, 26, 31, 44, 54, 55, 77, 93]),([2, 3, 2, 88, 3, 7, 10, 25, 1, 91],0,9,[1, 2, 2, 3, 3, 7, 10, 25, 88, 91])]
      
      def test_merge_sort(self):
          for test_data,start,end,expected in self.data:
              actual =quick_sort(test_data,start,end)
              self.assertEqual(actual,expected) 
    
if __name__=="__main__":
    start_time = time.time()
    unittest.main()
    print("--- %s seconds ---" % (time.time() - start_time))
