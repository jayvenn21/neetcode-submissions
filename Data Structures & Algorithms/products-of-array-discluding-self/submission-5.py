class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        l_mul = 1
        for i in range(0, len(nums), 1):
            res[i] = l_mul
            l_mul = res[i] * nums[i]
        r_mul = 1
        for j in range(len(nums) - 1, -1, -1):
            res[j] *= r_mul
            r_mul *= nums[j]
        return res