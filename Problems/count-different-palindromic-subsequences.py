# The previous three solutions try to find all the different palindromic subsequences solutions, so the runtime and memory are depend on how much the amount is.
# The last solution finds the number of different palindromic subsequences without recoding them.

# recursion
    # runtime: ?
    # memory: ?
    # Time Limit Exceeded!!!

class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:
        return len(self.find(S)) % (10**9+7)
        
    def find(self, s):
        if s=='':
            return set()
        if len(s)==1:
            return set(s[0])
        if s[0]==s[-1]:
            temp = self.find(s[1:-1])
            return set({s[0],s[0]+s[0]})|temp|{s[0]+_+s[0] for _ in temp}
        return self.find(s[0:-1])|self.find(s[1:])


# dynamic programming
    # runtime: ?
    # memory: ?
    # Memory Limit Exceeded!!!

class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:
        if len(S)<=1:
            return len(S)
        DP = [[set() for _ in range(len(S)+1)],
              [set(S[i]) for i in range(len(S))]+[set()]]
        for length in range(2,len(S)+1):
            for start in range(len(S)-length+1):
                if S[start]==S[start+length-1]:
                    DP[length%2][start] = ({S[start],S[start]+S[start]} |
                                           DP[length%2][start+1] |
                                           {S[start]+_+S[start] for _ in DP[length%2][start+1]})
                else:
                    DP[length%2][start] = DP[(length-1)%2][start]|DP[(length-1)%2][start+1]
        return len(DP[len(S)%2][0])%(10**9+7)


# search possible palindromic subsequences
    # runtime: ?
    # memory: ?
    # Time Limit Exceeded!!!

class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:
        lenS = len(S)
        if lenS<=1:
            return lenS
        ans = set(S)
        length = 0
        temp = set([''])
        while length<=lenS//2:
            new_temp = set()
            for string in temp:
                start = 0
                end = lenS-1
                find = 0
                while find<length:
                    while S[start]!=string[find]:
                        start += 1
                    while S[end]!=string[find]:
                        end -= 1
                    find += 1
                    start += 1
                    end -= 1
                search = S[start:end+1]
                for _ in set(search):
                    ans |= {string[:length]+_+string[length:]}
                count = {'a':0,'b':0,'c':0,'d':0}
                for alphabet in search:
                    count[alphabet] += 1
                for alphabet in count.keys():
                    if count[alphabet]>=2:
                        new_temp |= {string[:length]+alphabet+alphabet+string[length:]}
            ans |= new_temp
            temp = new_temp
            length += 1
            new_temp = set()             
        return len(ans)%(10**9+7)


# 
    # runtime: O(n^2)
    # memory: O(n^2)

class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:
        lenS = len(S)
        if lenS<=1:
            return lenS
        record = {}
        PREV = [-1 for i in range(lenS)]
        NEXT = [lenS for i in range(lenS)]
        for index,alphabet in enumerate(S):
            if alphabet in record:
                PREV[index] = record[alphabet]
                NEXT[record[alphabet]] = index
            record[alphabet] = index
        DP = [[1,2]+[0 for i in range(lenS-2)] for j in range(lenS)]
        for length in range(3,lenS+1):
            for start in range(lenS-length+1):
                end = start+length-1
                if S[start]!=S[end]:
                    DP[start][length-1] = DP[start][length-2]+DP[start+1][length-2]-DP[start+1][length-3]
                else:
                    if NEXT[start]==end:
                        DP[start][length-1] = 2*DP[start+1][length-3]+2
                    elif NEXT[start]==PREV[end]:
                        DP[start][length-1] = 2*DP[start+1][length-3]+1
                    else:
                        DP[start][length-1] = 2*DP[start+1][length-3]-DP[NEXT[start]+1][PREV[end]-NEXT[start]-2]
        return DP[0][lenS-1]%(10**9+7)