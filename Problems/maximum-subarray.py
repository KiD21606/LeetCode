# linear search
    # runtime: O(n)
    # memory: O(1)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        summ = 0
        for num in nums:
            summ += num
            if summ>result:
                result = summ
            if summ<0:
                summ = 0
            print(num, result)
        return result


# divide and conquer
    # runtime: O(log n)
    # memory: O(log n)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.Divide(nums)[3]

    def Divide(self, nums):
        if len(nums)==1:
            num = nums[0]
            return [num,num,num,num]
        else:
            return self.Conquer(self.Divide(nums[:len(nums)//2]), 
                                self.Divide(nums[len(nums)//2:]))

    def Conquer(self, result1, result2):
        summ = result1[0]+result2[0]
        left = max(result1[1],result1[0]+result2[1])
        right = max(result2[2],result2[0]+result1[2])
        maximum = max(result1[3],result2[3],result1[2]+result2[1])
        return [summ,left,right,maximum]

                