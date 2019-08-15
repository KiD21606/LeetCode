# 
    # runtime: O(2^n)
    # memory: O(2^n)
    # Let s[i] be the answer of n=i, then the runtime is O(len(s[1])+len(s[2])+...+len(s[n-1])).
    # Since each len(s[i]) is bounded by 2^i, the runtime is O(2^n).
    # The memory is O(len(s[n])) => O(2^n) too.

class Solution(object):
    def countAndSay(self, n):
        output = '1'
        for i in range(1,n):
            new_output = ''
            loc = 1
            pointer = 0
            end = len(output)
            while loc<end:
                if output[loc]!=output[pointer]:
                    new_output += str(loc-pointer)+output[pointer]
                    pointer = loc
                loc += 1
            new_output += str(loc-pointer)+output[pointer]
            output = new_output
        return output