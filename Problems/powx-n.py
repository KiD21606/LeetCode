# 
    # runtime: O(log n)
    # memory: O(log n)

class Solution(object):
    def myPow(self, x, n):
        if n==0:
            return 1
        if n==1:
            return x
        if n==-1:
            return 1/x
        elif n%2==0:
            return self.myPow(x*x,n//2)
        else:
            return self.myPow(x*x,n//2)*x
