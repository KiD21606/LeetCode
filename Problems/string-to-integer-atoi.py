# 
    # runtime: O(n)
    # memory: O(n)

class Solution:
    def myAtoi(self, str: str) -> int:
        n = len(str)
        if n==0:
            return 0
        ans = 0
        negative = False
        index = 0
        while index<n and str[index]==' ':
            index += 1
        if index==n:
            return 0
        if str[index]=='-':
            negative = True
            index += 1
        elif str[index]=='+':
            index += 1
        while index<n:
            num = ord(str[index])
            if 48<=num<=57:
                ans = 10*ans+num-48
                index += 1
            else:
                break
        if negative:
            return max(-ans,-(2**31))
        else:
            return min(ans,2**31-1)