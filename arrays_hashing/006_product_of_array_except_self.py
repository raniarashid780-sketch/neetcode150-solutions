class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [1] * n
        running_prefix = 1
        for i in range(n):
            res[i] = running_prefix
            running_prefix *= nums[i]
        running_suffix = 1
        for i in range(n-1, -1, -1):
            res[i] *= running_suffix
            running_suffix *= nums[i]
        return res
