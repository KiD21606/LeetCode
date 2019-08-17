# 
    # runtime: O(n^2)
    # memory: O(1)

class Solution:
    def countSubstrings(self, s: str) -> int:
        if s=='':
            return 0
        ans = 0
        for mid in range(len(s)):
            ans += 1
            width = 1
            while width<=min(mid,len(s)-mid-1):
                if s[mid-width]==s[mid+width]:
                    ans += 1
                    width += 1
                else:
                    break
        for mid in range(len(s)):
            width = 0
            while width<=min(mid,len(s)-mid-2):
                if s[mid-width]==s[mid+width+1]:
                    ans += 1
                    width += 1
                else:
                    break
        return ans