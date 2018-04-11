import unittest
'''
Given an array of n positive integers and a positive integer s, 
find the minimal length of a subarray of which the sum >= s. If there isn't one, return -1 instead.
'''
def minimumSize(nums, s):
            if not nums:
               return -1
            left =0
            right =0
            minlen =len(nums)+1
            sum =0
            while right < len(nums):
                  sum+= nums[right]
                  while sum >=s:
                        minlen = min(minlen,right -left+1)
                        sum =sum -nums[left]
                        left+=1
                  right+=1
            if minlen ==len(nums)+1:
               return-1
            else: 
                return minlen
class Test(unittest.TestCase):
      data =[([2,3,1,2,4,3],7,2),([9,1,8,2,7,3,6,4,5,10],55,10)]

      def test_binarySearch(self):
          for test_data,target,expected in self.data:
              actual = minimumSize(test_data,target)
              self.assertEqual(actual,expected)

if __name__=="__main__":
    unittest.main()
