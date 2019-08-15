# 
    # runtime: O(log n)
    # memory: O(1)

class Solution(object):
    def firstBadVersion(self, n):
        left = -1
        right = n
        while right>left+1:
            mid = (left+right)//2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid
        return right
        