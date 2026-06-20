class Solution:
    def isValid(self, s: str) -> bool:
        hashmap={")":"(","]":"[","}":"{"}
        stack=[]
        for para in s:
            if para in hashmap:
                if stack and stack[-1]==hashmap[para]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(para)
        return True if not stack else False
                

        