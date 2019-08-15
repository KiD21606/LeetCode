# 
    # runtime: O(max(m,n))
    # memory: O(max(m,n))

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a)>len(b):
            a,b = b,a
        carry = '0'
        ans = ''
        for i in range(1, len(a)+1):
            summ = a[-i]+b[-i]+carry
            if summ in ['000']:
                ans = '0'+ans
                carry = '0'
            elif summ in ['100','010','001']:
                ans = '1'+ans
                carry = '0'
            elif summ in ['110','101','011']:
                ans = '0'+ans
                carry = '1'
            else:
                ans = '1'+ans
                carry = '1'
        for i in range(len(a)+1,len(b)+1):
            if carry=='0':
                ans = b[:-i+1]+ans
                break
            elif b[-i]=='1':
                ans = '0'+ans
                carry = '1'
            else:
                ans = '1'+ans
                carry = '0'
        if carry=='1':
            ans = '1'+ans
        return ans