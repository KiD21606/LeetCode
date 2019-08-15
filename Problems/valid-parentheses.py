# 
    # runtime: O(n)
    # memory: O(1)

class Solution(object):
    def isValid(self, s):
        left = []
        right = {')':'(',
                 ']':'[',
                 '}':'{'
                }
        for _ in s:
            if _ not in right.keys():
                left.append(_)
            else:
                if left==[] or right[_]!=left.pop():
                    return False
        if left==[]:
            return True
        else:
            return False