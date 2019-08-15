# 
    # runtime: O(log n)
    # memory: O(1)

class Solution(object):
    def mySqrt(self, x):
        if x<=1: return x
        # Now we can garantee i<=sqrt(x)<j
        i,j = 0,x
        while i+1<j:
            mid = (i+j)//2
            if mid**2>x:
                j = mid
            elif mid**2<x:
                i = mid
            else:
                return mid
        return i