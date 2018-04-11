#!/usr/bin/python
import unittest
import time
'''
#  Given a disordered list of integers, rearrange them in natural order.
#
#  Sample Input: [18,5,100,3,1,19,6,0,7,4,2]
#
#  Sample Output: [0,1,2,3,4,5,6,7,18,19,100]
#
#  Time Complexity of Solution:
#  Best Case O(kn); Average Case O(kn); Worst Case O(kn),
#  where k is the length of the longest number and n is the
#  size of the input array.
#
#  Note: if k is greater than log(n) then an nlog(n) algorithm would
#  be a better fit. In reality we can always change the radix
#  to make k less than log(n).
#
#  Approach:
#  radix sort, like counting sort and bucket sort, is an integer based
#  algorithm (i.e. the values of the input array are assumed to be
#  integers). Hence radix sort is among the fastest sorting algorithms
#  around, in theory. The particular distinction for radix sort is
#  that it creates a bucket for each cipher (i.e. digit); as such,
#  similar to bucket sort, each bucket in radix sort must be a
#  growable list that may admit different keys.
#
#  For decimal values, the number of buckets is 10, as the decimal
#  system has 10 numerals/cyphers (i.e. 0,1,2,3,4,5,6,7,8,9). Then
#  the keys are continuously sorted by significant digits.
'''
def radix_sort(array):
    # initialize
    radix =10
    maxlen =False
    temp =-1
    placement =1
    while not maxlen:
          # create empty buckets
          maxlen = True
          buckets =[list() for i in range(radix)]
          # extract elements
          for item in array:
              temp =item/placement
              index =temp%radix
              buckets[index].append(item)
              if maxlen and temp >0:
                 maxlen =False
          # put it back in array
          array_index =0
          for bucket in range(radix):
                for item in buckets[bucket]:
                    array[array_index] =item
                    array_index+=1
            #next pass till the maxlen
          placement*=radix
    return array                 



class Test(unittest.TestCase):
      data =[([ 170, 45, 75, 90, 802, 24, 2, 66],[2, 24, 45, 66, 75, 90, 170, 802] ),([2, 3, 2, 88, 3, 7, 10, 25, 1, 91],[1, 2, 2, 3, 3, 7, 10, 25, 88, 91])]
      
      def test_radix_sort(self):
          for test_data,expected in self.data:
              actual =radix_sort(test_data)
              self.assertEqual(actual,expected) 
    
if __name__=="__main__":
    start_time = time.time()
    unittest.main()
    print("--- %s seconds ---" % (time.time() - start_time))
