class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans={}
        for i,num in enumerate(nums):
            remain=target-num
            if remain in ans:
                return [ans[remain],i]
            ans[num]=i
        return [0,0]
        