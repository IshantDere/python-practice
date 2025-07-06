# [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0] sorted arrey

# def find_num(cards, query):
#     location = 0

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y = str(x)
        
        list1 = []
        list2 = []

        for i in y, reversed(y):
            list1.append(i)
            list2.append(i)
 

        if list1 == list2:
            return True
        else:
            return False

x = 121
a = Solution()
b = a.isPalindrome(x)
print(b) 