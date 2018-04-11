import unittest

'''
Longest_Substring_Without_Repeating_Characters
'''
def lswrc(s):
    if not s:
            return 0
    if len(s)==1:
           return 1
    char_dict ={}
    max_len =0
    prev_index =-1
    for i in range(len(s)):
        if s[i] in char_dict and prev_index < char_dict[s[i]]:
             prev_index = char_dict[s[i]]
        length = i-prev_index
        max_len =max(max_len,length)
        char_dict[s[i]] =i
    return max_len 
   
class Test(unittest.TestCase):
      data =[("abcabcbb",3)]

      def test_lswrc(self):
          for test_string,expected in self.data:
              actual = lswrc(test_string)
              self.assertEqual(actual,expected)

if __name__=="__main__":
    unittest.main()
