#!/usr/bin/python
import unittest

def movezeros(array):
        i =0
        j =1
        while i <len(nums)-1 and j<len(nums):
              if nums[i] !=0 :
                 i+=1
                 j+=1
              elif nums[i]== 0 and nums[j] ==0:
                    j+=1
              elif nums[i] ==0 and nums[j]!=0:
                  temp = nums[i] 
                  nums[i] =nums[j] 
                  nums[j] =temp
                  i+=1
                  j+=1
        return nums


class Test:
          data =[[0, 1, 0, 3, 12],[1, 3, 12, 0, 0]]
          def test_movezeros(self):
              for a1,expected in self.data:
                  actual =movezeros(a1)
                  self.assertTrue(actual)

if __name__ == "__main__":

    unittest.main()
