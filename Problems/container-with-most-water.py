# 
    # runtime: O(n)
    # memory: O(1)

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        best_capacity = 0
        best_left_height = 0
        best_right_height = 0
        index_left = 0
        index_right = n-1
        while index_left<index_right:
            left_height = height[index_left]
            right_height = height[index_right]
            if left_height<best_left_height:
                index_left += 1
            elif right_height<best_right_height:
                index_right -= 1
            else:
                capacity = (index_right-index_left)*min(left_height,right_height)
                if capacity>best_capacity:
                    best_capacity = capacity
                    best_left_height = left_height
                    best_right_height = right_height
                if left_height<=right_height:
                    index_left += 1
                else:
                    index_right -= 1
        return best_capacity