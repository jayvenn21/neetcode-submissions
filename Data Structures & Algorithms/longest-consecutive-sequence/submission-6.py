class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        max_length = 0
        found = set(nums)
        for i in range(len(nums)):
            if nums[i] - 1 not in found:
                length = 1
                while nums[i] + length in found:
                    length += 1
                max_length = max(max_length, length)
        return max_length
            

        