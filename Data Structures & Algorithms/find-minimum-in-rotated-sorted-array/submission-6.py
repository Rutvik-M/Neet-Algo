class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum=float("inf")
        for num in nums:
            minimum=min(minimum,num)
        return minimum


        