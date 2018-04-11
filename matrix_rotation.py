#!/usr/bin/python
import unittest


def matrix_rotation(matrix):
#   matrix_length = len(matrix)
#   matrix_width =len(matrix[0])
#   if matrix_length ==0 or matrix_length!=matrix_width:
#     return False
#   else:
       n = len(matrix)
      
       for layer in range(n // 2):
           first = layer
           last  =  n - layer - 1
           for i in range(first,last):
               # get top
              top= matrix[layer][i]
              #top = matrix[layer][i] 

               # left to top
              matrix[layer][i]= matrix[-i - 1][layer] 
              #matrix[layer][i] = matrix[-i - 1][layer]

               # bottom to left
              matrix[-i - 1][layer] =matrix[-layer - 1][-i - 1]
              #matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

               #right to bottom
              matrix[-layer - 1][-i - 1] =matrix[i][-layer - 1]

              matrix[-layer - 1][-i - 1] = matrix[i][-layer - 1]

               # top to right
              matrix[i][- layer - 1] = top

              #matrix[i][- layer - 1] = top
       return matrix  
      
class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ])
    ]

    def test_rotate_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = matrix_rotation(test_matrix)
            self.assertEqual(actual, expected)
if __name__=="__main__":
     unittest.main()


