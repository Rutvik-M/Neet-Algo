class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")":"(","]":"[","}":"{"}
        stack = []

        for bracket in s:
            if bracket in brackets:
                if stack and stack[-1] == brackets[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        if len(stack)==0:
            return True
        else:
            return False

        