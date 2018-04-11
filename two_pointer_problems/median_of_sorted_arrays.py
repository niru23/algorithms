#!/usr/bin/python
import unittest
# just doing merge portion of merge sort but this takes in m+n space. where m and n are lengths of array1, array2 respectively.
def median(array1,array2):
    n1 =len(array1)
    n2 =len(array2)
    final =[None]*(n1+n2)
    i =0
    j =0
    k =0
    while i < n1 and j<  n2:
          if array1[i] <=array2[j]:
             final[k]=array1[i]
             i+=1
             k+=1
          else:
                final[k]=array2[j]
                j+=1
                k+=1
    while i < n1:
          final[k]=array1[i]
          i+=1
          k+=1
    while  j < n2:
           final[k]=array2[j]
           j+=1
           k+=1
    print final
    print k
    print final[k//2]
    print final[k//2 -1]
    if k%2 ==0:
       return float(final[k//2]+final[k//2 -1])/2
    else:
       return final[k//2]



class Test:
      data =[([1, 2, 3, 4, 5],[2, 3, 4, 5, 6],3.5),([100,200],[1,4,250,300,400],200)]
      def test_median(self):
	          for test_array1,test_array2,expected in self.data:
	              actual = median( test_array1,test_array2)
	              self.assertEqual(actual,expected)
      
if __name__=="__main__":
   unittest.main()  
