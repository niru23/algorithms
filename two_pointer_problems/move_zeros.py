import unittest
'''
intersection of arrays with duplicates
'''
def move_zeros(array):
    i =0
    j =1
    while i < len(array)-1 and j < len(array):
          if array[i]!=0:
             i+=1
             j+=1
          elif array[i]==0 and array[j]==0:
             j+=1
          elif array[i]==0 and array[j]!=0:
             temp =array[i]
             array[i]=array[j]
             array[j]=temp
             i+=1
             j+=1
    return array


class Test(unittest.TestCase):
      data =[([0, 1, 0, 3, 12],[1, 3, 12, 0, 0])]

      def test_binarySearch(self):
          for test_arr,expected in self.data:
              actual = move_zeros(test_arr)
              self.assertEqual(actual,expected)

if __name__=="__main__":
    unittest.main()
