class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        forS1=[0]*26
        forS2 = [0]*26
        left=0
        for ch in s1:
            forS1[ord(ch)-ord("a")]+=1
        for i in range(len(s1)):
            forS2[ord(s2[i])-ord("a")]+=1
        if forS1==forS2:
            return True
        for right in range(len(s1),len(s2)):
            forS2[ord(s2[right])-ord("a")]+=1
            forS2[ord(s2[left])-ord("a")]-=1
            left+=1
            if forS1==forS2:
                return True
        return False
        