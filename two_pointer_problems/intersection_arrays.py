import unittest
'''
intersection of arrays with duplicates
'''
def intersection_array_using_pointers(array1,array2):
    arr1=sorted(array1)
    arr2= sorted(array2)
    intersect =[]
    i =0
    j=0
    while i< len(arr1) and j<len(arr2):
          if arr1[i] < arr2[j]:
             i+=1
          elif arr1[i] < arr2[j]:
             j+=1
          elif arr1[i] == arr2[j]:
               intersect.append(arr1[i])
               i+=1
               j+=1
    return intersect


class Test(unittest.TestCase):
      data =[([1, 2, 2, 1],[2, 2],[2, 2])]

      def test_binarySearch(self):
          for test_arr1,test_arr2,expected in self.data:
              actual = intersection_array_using_pointers(test_arr1,test_arr2)
              self.assertEqual(actual,expected)

if __name__=="__main__":
    unittest.main()
