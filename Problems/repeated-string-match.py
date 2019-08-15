# 
    # runtime: O(m(m+n)) n=len(A), m=len(B)
    # memory: O(m+n)
    # (see https://leetcode.com/problems/repeated-string-match/solution/)

class Solution(object):
    def repeatedStringMatch(self, A, B):
        n = (len(B)-1)//len(A) +1
        for ans in range(n,n+2):
            if B in A*ans:
                return ans
        return -1
