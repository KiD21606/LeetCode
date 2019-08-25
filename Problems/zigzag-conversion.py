# 
    # runtime: O(n)
    # memory: O(n)

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = ['' for _ in range(numRows)]
        if s=='' or numRows==1:
            return s
        n = len(s)
        index_s = 0
        index_r = 0
        while index_s<n:
            while index_s<n and index_r<numRows-1:
                rows[index_r] += s[index_s]
                index_r += 1
                index_s += 1
            while index_s<n and index_r>0:
                rows[index_r] += s[index_s]
                index_r -= 1
                index_s += 1
        return ''.join(rows)