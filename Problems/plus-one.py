# 
    # runtime: O(n)
    # memory: O(n)

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(1,len(digits)+1):
            if digits[-i]==9:
                digits[-i] = 0
            else:
                digits[-i] += 1
                carry = 0
                break
        if carry:
            digits = [1] + digits
        return digits
            