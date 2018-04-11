#!/usr/bin/python
import unittest
'''
Given two arrays, write a function to compute their intersection.
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

For union of two arrays, follow the following merge procedure.
1) Use two index variables i and j, initial values i = 0, j = 0
2) If arr1[i] is smaller than arr2[j] then print arr1[i] and increment i.
3) If arr1[i] is greater than arr2[j] then print arr2[j] and increment j.
4) If both are same then print any of them and increment both i and j.
5) Print remaining elements of the larger array.



For Intersection of two arrays, print the element only if the element is present in both arrays.
1) Use two index variables i and j, initial values i = 0, j = 0
2) If arr1[i] is smaller than arr2[j] then increment i.
3) If arr1[i] is greater than arr2[j] then increment j.
4) If both are same then print any of them and increment both i and j.

'''
def intersection(nums1, nums2):
        result =[]
        arr1 =sorted(nums1)
        arr2 =sorted(nums2)
        i =0
        j= 0
        while (i < len(arr1) and j <len(arr2)):
              if arr1[i] < arr2[j]:
                  i+=1
              elif arr1[i] > arr2[j]:
                  j+=1
              else:
                   result.append(arr1[i])
                   i+=1
                   j+=1
        return result


def union(nums1, nums2):
    result =[]
    arr1 =sorted(nums1)
    arr2 =sorted(nums2)
    i =0
    j= 0
    while (i < len(arr1) and j <len(arr2)):
          if arr1[i] < arr2[j]:
             result.append(arr1[i])
             i+=1
          elif arr1[i] > arr2[j]:
             result.append(arr2[j])
             j+=1
          else:
              result.append(arr2[j])
              i+=1
              j+=1
    while i < len(arr1):
          result.append(arr1[i])
          i+=1
    while j < len(arr2):
          result.append(arr2[j])
          j+=1
    return result



class Test:
          data =[([5,25,4,39,57,49,93,79,7,8,49,89,2,7,73,88,45,15,34,92,84,38,85,34,16,6,99,0,2,36,68,52,73,50,77,44,61,48],[61,24,20,58,95,53,17,32,45,85,70,20,83,62,35,89,5,95,12,86,58,77,30,64,46,13,5,92,67,40,20,38,31,18,89,85,7,30,67,34,62,35,47,98,3,41,53,26,66,40,54,44,57,46,70,60,4,63,82,42,65,59,17,98,29,72,1,96,82,66,98,6,92,31,43,81,88,60,10,55,66,82,0,79,11,81],[0, 4, 5, 6, 7, 34, 38, 44, 45, 57, 61, 77, 79, 85, 88, 89, 92])]
          data1 =[([1, 2, 4, 5, 6],[2, 3, 5, 7],[1, 2, 3, 4, 5, 6, 7])]
   
          def test_intersection(self):
              for a1,a2,expected in self.data:
                  actual =intersection(test_string)
                  self.assertTrue(actual)
          def test_union(self):
              for a1,a2,expected in self.data1:
                  actual =intersection(test_string)
                  self.assertTrue(actual)

if __name__ == "__main__":

    unittest.main()
         







