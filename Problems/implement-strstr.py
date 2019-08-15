# brute-force
    # runtime: O(mn)
    # memory: O(1)

class Solution(object):
    def strStr(self, haystack, needle):
        if needle=='':
            return 0
        n = len(haystack)
        m = len(needle)
        for i in range(n-m+1):
            if haystack[i:i+m]==needle:
                return i
        return -1