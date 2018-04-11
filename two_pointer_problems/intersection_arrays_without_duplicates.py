import unittest
'''
intersection of arrays with duplicates
'''
def intersection_array_using_sets(array1,array2):
    arr1=set(array1)
    arr2= set(array2)
    return list(arr1 &arr2)


class Test(unittest.TestCase):
      data =[([1, 2, 2, 1],[2, 2],[2])]

      def test_binarySearch(self):
          for test_arr1,test_arr2,expected in self.data:
              actual = intersection_array_using_sets(test_arr1,test_arr2)
              self.assertEqual(actual,expected)

if __name__=="__main__":
    unittest.main()
