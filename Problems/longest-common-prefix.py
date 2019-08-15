# vertical scanning
    # runtime: O(mn) m = len(input), n = minimum length of strings in input
    # memory: O(1)

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        n = len(strs)
        if n==0:
            return ''
        if n==1:
            return strs[0]
        m = min([len(s) for s in strs])
        for i in range(m):
            letter = strs[0][i]
            for j in range(1,n):
                if strs[j][i]!=letter:
                    return strs[0][:i]
        return strs[0][:m]
