class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # key value pair
        found = defaultdict(int)
        print(found)
        for i in range(len(nums)):
            part = target - nums[i]
            if part in found:
                return [found[part], i]
            found[nums[i]] = i
        
        

        