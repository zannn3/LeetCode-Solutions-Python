# method 1: two pointers, modify in place
class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if not A:
            return []
        left, right = 0, len(A)-1
        while left < right:
            if A[left] %2 == 0:
                left += 1
            elif A[right] % 2 == 1:
                right -= 1
            else:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
        return A
    


"""
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
 

Note:

1 <= A.length <= 5000
0 <= A[i] <= 5000
"""
