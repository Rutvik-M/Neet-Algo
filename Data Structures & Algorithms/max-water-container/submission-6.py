class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        longest=0
        while left<right:
            minimum=min(heights[left],heights[right])
            area=minimum*(right-left)
            longest=max(longest,area)
            if heights[left]<=heights[right]:
                left+=1
            else:
                right-=1
        return longest


        