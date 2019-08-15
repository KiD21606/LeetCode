# 
    # runtime: O(log(min(m,n)))
    # memory: O(1)

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        if len(nums1)>len(nums2):
            nums1, nums2, len1, len2 = nums2, nums1, len2, len1
        if len1==0:
            return (nums2[len2//2]+nums2[(len2-1)//2])/2
        n = len1+len2
        odd = n%2
        left = 0
        right = len1
        while left<right:
            index1 = (left+right)//2
            index2 = (n+odd)//2-index1
            if index2<0:
                right = index1-1
            elif index2>len2:
                left = index1+1
            elif index1>0 and nums1[index1-1]>min(nums1[index1:]+nums2[index2:]):
                right = index1-1
            elif index2>0 and nums2[index2-1]>min(nums1[index1:]+nums2[index2:]):
                left = index1+1
            else:
                left = index1
                break
        LEFT = [nums1[left-1], nums2[(n+odd)//2-left-1]]
        RIGHT = [nums1[left], nums2[(n+odd)//2-left]]
        if odd:
            return max(LEFT)
        else:
            return (max(LEFT)+min(RIGHT))/2
        
        
        
