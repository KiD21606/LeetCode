# brute force
    # runtime: O(n^2)
    # memory: O(1)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        test = 1
        start = 0
        while start+test<=n and start+ans<=n:
            if len(set(s[start:start+test]))<test:
                start += 1
            else:
                ans = test
                test += 1
        return ans

# sliding window
    # runtime: O(n)
    # memory: O(1)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        start = 0
        end = 0
        chars = set()
        while end<n:
            if s[end] not in chars:
                chars |= {s[end]}
                end += 1
                ans = max(ans,end-start)
            else:
                chars -= {s[start]}
                start += 1
        return ans
