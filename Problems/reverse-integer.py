# 
    # runtime: O(log(x))
    # memory: O(1)

class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        if x<0:
            negative = True
            x = -x
        else:
            negative = False
        while x:
            x, res = x//10, x%10
            ans = 10*ans+res
        if negative:
            ans = -ans
        if ans>2**31-1 or ans<-2**31:
            return 0
        return ans
        