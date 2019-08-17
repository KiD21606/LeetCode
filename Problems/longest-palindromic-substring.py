# 
    # runtime: O(n^2)
    # memory: O(1)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s=='':
            return ''
        best = [0,0]
        odd = True
        length = 1
        # odd     # *...*(mid)*...*
        for mid in range(len(s)):
            width = 1
            while width<=min(mid,len(s)-1-mid):
                if s[mid-width]==s[mid+width]:
                    if 2*width+1>length:
                        length = 2*width+1
                        best = [mid, width]
                    width += 1
                else:
                    break
        # even    # *...*(mid)(mid+1)*...*
        if len(s)>=2:
            for mid in range(len(s)-1):
                width = 0
                while width<=min(mid,len(s)-mid-2):
                    if s[mid-width]==s[mid+1+width]:
                        if 2*width+2>length:
                            length = 2*width+2
                            best = [mid, width]
                            odd = False
                        width += 1
                    else:
                        break
        if odd:
            return s[best[0]-best[1]:best[0]+best[1]+1]
        else:
            return s[best[0]-best[1]:best[0]+best[1]+2]