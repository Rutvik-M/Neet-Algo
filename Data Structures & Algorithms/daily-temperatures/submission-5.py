class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[0]*len(temperatures)
        stack=[]

        for i,temp in enumerate(temperatures):
            count=0
            while stack and temp>temperatures[stack[-1]]:
                idx=stack.pop()
                ans[idx]=i-idx
            stack.append(i)

        return ans

        