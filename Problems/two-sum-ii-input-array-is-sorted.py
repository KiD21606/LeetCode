# 
    # runtime: O(n)
    # memory: O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = len(numbers)-1
        summantion = numbers[index1]+numbers[index2]
        while summantion!=target:
            if summantion<target:
                index1 += 1
            else:
                index2 -= 1
            summantion = numbers[index1]+numbers[index2]
        return [index1+1,index2+1]