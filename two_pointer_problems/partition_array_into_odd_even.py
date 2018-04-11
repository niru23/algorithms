import unittest
'''
partition array into odd and even
'''
def partition_odd_even(array):
         # write your code here
     start =0
     end = len(array)-1
     while start <= end:
           while array[start]%2==1:
              start+=1
           while array[end]%2==0:
              end-=1
           if start < end:
              temp = array[start]
              array[start] =array[end]
              array[end]=temp  
     return array
class Test(unittest.TestCase):
      data =[([1, 2, 3, 4],[1, 3, 2, 4])]

      def test_binarySearch(self):
          for test_data,expected in self.data:
              actual = partition_odd_even(test_data)
              self.assertEqual(actual,expected)

if __name__=="__main__":
    unittest.main()
