class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        if nums[0] < nums[-1]:  # not rotated
            return nums[0]
        
        left, right = 0, len(nums)-1
        
        while left + 1 < right:
            mid = left + (right-left)//2
            if nums[mid] > nums[mid+1]:  # pivot found
                return nums[mid+1]
            if nums[mid] > nums[left]:
                left = mid
            else:
                right = mid
        
        return min(nums[left], nums[right])

"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
"""
