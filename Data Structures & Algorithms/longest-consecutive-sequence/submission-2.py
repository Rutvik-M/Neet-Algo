class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        max_seq=0
        for num in numSet:
            if num-1 not in numSet:
                count=1
                while num+count in numSet:
                    count+=1
                max_seq=max(max_seq,count)
        return max_seq


        