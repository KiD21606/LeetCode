# use split()
    # runtime: O(n)
    # memory: O(n)

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        ans = ''
        for string in s:
            for index in range(1,len(string)+1):
                ans += string[-index]
            ans += ' '
        return ans[:-1]


# do not use split()
    # runtime: O(n)
    # memory: O(n)

class Solution:
    def reverseWords(self, s: str) -> str:
        start = 0
        end = 0
        n = len(s)
        ans = ''
        while end<n-1:
            end = start
            while end<n-1 and s[end+1]!=' ':
                end += 1
            for i in range(end,start-1,-1):
                ans += s[i]
            start = end+1
            while start<n and s[start]==' ':
                ans += ' '
                start += 1
        return ans