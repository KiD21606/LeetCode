# longest common subsequence
    # runtime: O(n^2)
    # memory: O(n)
    # Time Limit Exceeded!!!

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if s=='':
            return 0
        LCS = [[0 for _ in range(len(s)+1)],[0 for _ in range(len(s)+1)]]
        for i in range(len(s)):
            for j in range(1,len(s)+1):
                if s[i]==s[-j]:
                    LCS[i%2][j] = LCS[(i-1)%2][j-1]+1
                else:
                    LCS[i%2][j] = max(LCS[(i-1)%2][j],LCS[i%2][j-1])
        return LCS[i%2][j]


# dynamic programming
    # runtime: O(n^2)
    # memory: O(n)

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if len(s)<=1:
            return len(s)
        DP = [[0 for _ in range(len(s)+1)],[1 for _ in range(len(s))]+[0]]
        print(DP[1])
        for length in range(2,len(s)+1):
            for start in range(len(s)-length+1):
                if s[start]==s[start+length-1]:
                    DP[length%2][start] = DP[length%2][start+1]+2
                else:
                    DP[length%2][start] = max(DP[(length-1)%2][start],
                                              DP[(length-1)%2][start+1])
        return DP[length%2][start]