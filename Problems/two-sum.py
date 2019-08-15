# exhaustive search
    # runtime: O(n^2)
    # memory: O(1)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for index1 in range(n):
            for index2 in range(index1+1,n):
                if nums[index1]+nums[index2] == target:                
                    return [index1, index2]
        