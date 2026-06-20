class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest=0
        for num in numSet:
            if num-1 not in numSet:
                count=1
                curr=num
                while curr+1 in numSet:
                    count+=1
                    curr+=1
                longest=max(count,longest)
        return longest


        