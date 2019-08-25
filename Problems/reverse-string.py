# 
    # runtime: O(n)
    # memory: O(1) extra memory

class Solution:
    def reverseString(self, s: List[str]) -> None:
        for index in range(len(s)//2):
            s[index], s[-index-1] = s[-index-1], s[index]
        return s