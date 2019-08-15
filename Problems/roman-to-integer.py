# 
    # runtime: O(n)
    # memory: O(1)

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        ROMAN = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,
                'IV':4,'XL':40,'CD':400,
                'IX':9,'XC':90,'CM':900}
        while s!='':
            if len(s)>1 and ( s[:2] in ROMAN.keys() ):
                ans += ROMAN[s[:2]]
                s = s[2:]
            else:
                ans += ROMAN[s[0]]
                s = s[1:]
        return ans
