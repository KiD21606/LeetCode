# 
    # runtime: O(log n)
    # memory: O(1)

class Solution(object):
    def guessNumber(self, n):
        left = -1
        right = n
        while right>left+1:
            mid = (left+right)//2
            if guess(mid)==-1:
                right = mid
            elif guess(mid)==1:
                left = mid
            else:
                return mid
        return right