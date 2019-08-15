# 
    # runtime: O(n^3)
    # memory: O(n^2)

class Solution(object):
    def getMoneyAmount(self, n):
        costs = {}
        # key:[start,end], value:minimum cost
        for i in range(1,n+1):
            costs[i,i] = 0
            costs[i,i+1] = i 
            costs[i,i+2] = i+1
        for j in range(3,n):
            for i in range(1,n-j+1):
                costs[i,i+j] = min([k+max(costs[i,k-1],costs[k+1,i+j]) 
                                    for k in range(i+j//2,i+j)
                                    ])
        return costs[1,n]