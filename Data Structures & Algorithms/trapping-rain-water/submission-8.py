class Solution:
    def trap(self, height: List[int]) -> int:
        # [0,2,0,3,1,0,1,3,2,1]
        l, r = 0, len(height) - 1
        res = 0
        maxLeft, maxRight = height[l], height[r]
        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(height[l], maxLeft)
                res += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(height[r], maxRight)
                res += maxRight - height[r]
        return res
        