# longest common subsequence 
    # runtime: O(mn)
    # memory: O(min(m,n))

class Solution:
    def minDistance(self, word1, word2):
        n1 = len(word1)
        n2 = len(word2)
        if n1<n2:
            word1, word2, n1, n2 = word2, word1, n2, n1
        table = [[0]*(n2+1),[0]*(n2+1)]
        for i1 in range(n1):
            for i2 in range(n2):
                table[(i1+1)%2][i2+1]=1
                if word1[i1]==word2[i2]:
                    table[(i1+1)%2][i2+1]=table[i1%2][i2]+1
                elif table[i1%2][i2+1]>table[(i1+1)%2][i2]:
                    table[(i1+1)%2][i2+1]=table[i1%2][i2+1]
                else:
                    table[(i1+1)%2][i2+1]=table[(i1+1)%2][i2]
        return n1+n2-2*table[n1%2][n2]