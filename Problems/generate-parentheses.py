# 
    # runtime: O(4^n/sqrt(n)) 
    # memory: O(4^n/sqrt(n))
    # (see https://leetcode.com/problems/generate-parentheses/solution/)

class Solution(object):
    def generateParenthesis(self, n):
        if n==0:
            return ['']
        else:
            return self.func([''],n,0)
    def func(self,ans,left,right):
        if left==0:
            if right==0:
                return ans
            else:
                return self.func([_+')' for _ in ans],left,right-1)
        else:
            if right==0:
                return self.func([_+'(' for _ in ans],left-1,right+1)
            else:
                return self.func([_+'(' for _ in ans],left-1,right+1) + self.func([_+')' for _ in ans],left,right-1)
            
# 
    # runtime: O(4^n/sqrt(n)) 
    # memory: O(4^n/sqrt(n))
    # (see https://leetcode.com/problems/generate-parentheses/solution/)

class Solution(object):
    def generateParenthesis(self, n):
        if n==0:
            return ['']
        ans = []
        def func(string,left,right):
            if len(string)==2*n:
                ans.append(string)
            if left<n:
                func(string+'(',left+1,right)
            if right<left:
                func(string+')',left,right+1)
        func('',0,0)
        return ans
    
            