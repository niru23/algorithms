import unittest
'''
valid_palindrom using two pointers
'''
def valid_palindrom(string):
    ispal =True
    char_list =[]
    for i in string:
        if i.isalnum():
           char_list.append(i.lower())
    start =0
    end = len(char_list)-1
    while start < end and ispal:
          if char_list[start] == char_list[end]:
             start+=1
             end-=1
          elif char_list[start] != char_list[end]: 
             ispal = False    
    return ispal  
# this can be done as

def valid_palindrom(string):
    char_list =[]
    for i in string:
        if i.isalnum():
           char_list.append(i.lower())
    return ''.join(char_list)==''.join(char_list[::-1]) 

class Test(unittest.TestCase):
      data =[("A man, a plan, a canal: Panama",True),("race a car",False)]

      def test_valid_palindrom(self):
          for test_string,expected in self.data:
              actual = valid_palindrom(test_string)
              self.assertEqual(actual,expected)

if __name__=="__main__":
    unittest.main()
