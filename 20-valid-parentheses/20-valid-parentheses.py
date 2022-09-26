class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        graph = {"(":")","{":"}","[":"]"}
        for i in s:
            if not stack:
                stack.append(i)
            else :
                if stack[-1] in graph:
                    if graph[stack[-1]] == i :
                        stack.pop()
                    else :
                        stack.append(i)
                else :
                    stack.append(i)
        if not stack:
            return True
        else :
            return False
        