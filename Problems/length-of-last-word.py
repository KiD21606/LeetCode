# 
    # runtime: O(n)
    # memory: O(1)

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        while s!='' and s[-1]==' ':
            s = s[:-1]
        for i in range(1,len(s)+1):
            if s[-i]==' ':
                return i-1
        return len(s)