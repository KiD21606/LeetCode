# 
    # runtime: O(n)
    # memory: O(n)

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        s = list(s)
        for partition in range(n//(2*k)+1):
            start = 2*k*partition
            end = min(start+k-1,n-1)
            while start<end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
        return ''.join(s)
        