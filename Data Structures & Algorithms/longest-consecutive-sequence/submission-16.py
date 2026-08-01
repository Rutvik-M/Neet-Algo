class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maximum=0
        numset=set(nums)
        for num in numset:
            if num-1 not in numset:
                cnt=1
                while num+cnt in numset:
                    cnt+=1
                maximum=max(cnt,maximum)
        return maximum
        