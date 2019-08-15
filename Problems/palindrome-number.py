# 
    # runtime: O(log(x))
    # memory: O(1)

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        x = str(x)
        while len(x)>1:
            if x[0]!=x[-1]:
                return False
            else:
                x = x[1:-1]
        return True
        